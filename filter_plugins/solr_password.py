#!/usr/bin/python

from base64 import b64encode
from hashlib import sha256
from os import urandom


def solrBasicAuthHash(password: str, salt: bytes):
    """
    Source: https://gist.github.com/OdyX/1513aacee2ca010dcf954d62af776469
    Python translation of
    https://github.com/apache/lucene-solr/blob/master/solr/core/src/java/org/apache/solr/security/Sha256AuthenticationProvider.java#L112
    """
    # Compute the SHA256 of (salt+password)
    m = sha256()
    m.update(salt)
    m.update(password.encode("utf-8"))
    # Compute the SHA256 of the previous
    # The solr hash is in fact sha256(sha256(salt+password))
    return sha256(m.digest()).digest()


def solrBasicAuthString(password: str, salt: bytes):
    """
    Return the full hash + salt as solr expects it
    """
    hashed = solrBasicAuthHash(password, salt)
    b64hashed = b64encode(hashed)
    b64salt = b64encode(salt)
    return f"{str(b64hashed, 'ascii')} {str(b64salt, 'ascii')}"


def solr_basicauth_filter(solr_pass, salt=None):

    # generate random salt if not passed
    if salt is None:
        bsalt = urandom(32)
    # or convert to bytes if string passed
    else:
        bsalt = salt.encode('utf-8')

    return solrBasicAuthString(solr_pass, bsalt)


class FilterModule(object):
    '''Generate Solr basic auth passwords'''

    def filters(self):
        return {'solr_basicauth': solr_basicauth_filter}

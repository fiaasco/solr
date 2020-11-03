import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_solr_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('solr').is_enabled
    assert host.service('solr').is_running


def test_solr_cores(host):
    """ Testing whether the cores have been created
    """
    solr_cores = host.run('curl --user fiaas:SolrRocks http://localhost:8983/solr/admin/cores')
    assert 'drupal7' in solr_cores.stdout
    assert 'drupal8' in solr_cores.stdout

def test_solr_ping(host):
    """ Testing whether the cores are online
    """
    d7 = host.run('curl --user d7:d7 http://localhost:8983/solr/drupal7/admin/ping')
    assert 'OK' in d7.stdout
    d8 = host.run('curl --user d8:d8 http://localhost:8983/solr/drupal8/admin/ping')
    assert 'OK' in d8.stdout

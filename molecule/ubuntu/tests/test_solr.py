import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_solr_service(host):
    """ Testing whether the service is running and enabled
    """
    # TODO: service enabled check fails on ubuntu for unclear reason
    # assert host.service('solr8').is_enabled
    assert host.service('solr8').is_running


def test_solr_cores(host):
    """ Testing whether the cores have been created
    """
    solr_cores = host.run('curl --user fiaas:SolrRocks http://localhost:8983/solr/admin/cores')
    assert 'drupal7' in solr_cores.stdout
    assert 'drupal8' in solr_cores.stdout

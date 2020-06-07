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
    solr_cores = host.run('curl http://localhost:8983/solr/admin/cores')
    assert 'drupal7' in solr_cores.stdout
    assert 'drupal8' in solr_cores.stdout

import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_elasticsearch_cluster(host):
    out = host.check_output(
        'curl -I  -k -u "elastic:my_password" https://127.0.0.1:9201/')
    assert '200' in out

def test_search_elastic_connection(host):
    out = host.check_output(
        'curl -I  -k -u "elastic:my_password" https://127.0.0.1:9201/image_keyvalue_pair_metadata_1')
    assert '200' in out

def test_searchengine_connection(host):
    out = host.check_output('curl -XGET http://127.0.0.1:5577/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out

def test_searchengine_connection(host):
    out = host.check_output('curl -XGET http://127.0.0.1:5577/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out


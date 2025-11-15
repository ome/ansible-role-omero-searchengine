import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nginx_gateway(host):
    out = host.check_output('curl -XGET http://127.0.0.1:8080/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out

def test_redis_connection(host):
    out = host.check_output('redis-cli ping')
    assert 'PONG' in out

def test_searchengine_connection(host):
    out = host.check_output('curl -XGET http://127.0.0.1:5577/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out

#def test_searchengine_elastic_cluster_health(host):
#    out = host.check_output('curl -XGET -k -u "elastic:elastic_password" https://127.0.0.1:9201/_cluster/health?pretty')
#    assert  '"status" : "green",' in out

#def test_searchengine_elasticsearch_connection(host):
#    out = host.check_output('curl -XGET -k -u "elastic:elastic_password" https://127.0.0.1:9201/image_keyvalue_pair_metadata_1 | | head -n1')
#    assert '"image_keyvalue_pair_metadata_1":{"aliases":' in out

def test_create_search_index(host):
    #out = host.check_output('curl -s -o /dev/null -w "%{http_code}"   -k -u "elastic:elastic_password" https://127.0.0.1:9201/image_keyvalue_pair_metadata_1')
    out = host.check_output(
        'curl -I  -k -u "elastic:elastic_password" https://127.0.0.1:9201/image_keyvalue_pair_metadata_1')
    assert '200' in out

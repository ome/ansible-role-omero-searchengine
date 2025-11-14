import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nginx_gateway(host):
    out = host.check_output('curl -L  http://127.0.0.1:80/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out

def test_redis_connection(host):
    out = host.check_output('redis-cli ping')
    assert 'PONG' in out

def test_searchengine_connection(host):
    out = host.check_output('curl -L  http://127.0.0.1:5577/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out

def test_searchengine_elastic_cluster_health(host):
    out = host.check_output('curl  -L -k -u "elastic:elastic_password" https://127.0.0.1:9201/_cluster/health?pretty')
    assert  '"status" : "green",' in out


#def test_searchengine_search_elastic_connection(host):
#    out = host.check_output('http://127.0.0.1:8080/searchengine//api/v1/resources/image/searchvaluesusingkey/?key=cell%20line')
#    assert  '"error"' in out

def test_searchengine_search_elastic_connection(host):
    out = host.check_output('curl -L -k -u  "elastic:elastic_password" https://127.0.0.1:9201/image_keyvalue_pair_metadata')
    assert '{"image_keyvalue_pair_metadata":{"aliases":{},"mappings":' in out


def test_searchengine_elastic_ports(host):
    out = host.check_output('lsof -i :9201')
    assert 'test to display port' in out

def test_searchengine_nginx_ports(host):
    out = host.check_output('lsof -i :80')
    assert 'Test to display ports' in out


#image_keyvalue_pair_metadata
import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nginx_gateway(host):
    out = host.check_output('curl -L  http://127.0.0.1:80/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out


def test_searchengine_gateway(host):
    out = host.check_output('curl -L  http://127.0.0.1:5577/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out
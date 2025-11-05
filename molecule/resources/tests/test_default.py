import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nginx_gateway(host):
    out = host.check_output('curl -L  https://localhost/searchengine/api/v1/resources/')
    assert 'OMERO search engine (API V1)' in out
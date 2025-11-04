import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nginx_gateway(host):
    out = host.check_output('curl -L  127.0.0.1/searchengine ')
    assert 'OMERO.web - Login' in out
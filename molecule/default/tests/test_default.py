import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'apt-transport-https',
    'signal-desktop',
])
def test_packages_installed(host, pkg):
    assert host.package(pkg).is_installed

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_apache2_is_instaled(host):
    assert host.package("apache2").is_installed

def test_apache2_is_enabled(host):
  assert host.service('apache2').is_enabled

def test_index_html(host):
    index_html = host.file("/var/www/html/index.html")
    assert index_html.user == "root"
    assert index_html.group == "root"

def test_is_user_exists(host):
    user = host.user("www-data")
    assert user.exists

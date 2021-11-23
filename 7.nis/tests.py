import subprocess


def test_domain():
    domain = subprocess.run(['domainname | grep nis.example.com'],stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,shell = True)
    assert domain.returncode == 0

def test_services():
    services = subprocess.run(['rpcinfo -p server| grep \'ypserv\|ypbind\|fypxfrd\|yppasswdd\''],stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,shell = True)
    assert services.returncode == 0

def test_nsswitch():
    nsswitch = subprocess.run(["cat /etc/nsswitch.conf | grep nis | grep 'passwd\|group'"],stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,shell = True)
    assert nsswitch.returncode == 0



test_domain()
test_services()
test_nsswitch()

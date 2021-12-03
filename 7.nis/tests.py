import subprocess


def test_domain():
    domain = subprocess.run(['ypdomainname | grep nis.example.com'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)
    assert domain.returncode == 0

def test_ypserv():
    services = subprocess.run(["rpcinfo -p server| grep ypserv"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)
    assert services.returncode == 0
def test_ypbind():
    services = subprocess.run(["rpcinfo -p server| grep ypbind"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)
    assert services.returncode == 0
def test_fypxfrd():
    services = subprocess.run(["rpcinfo -p server| grep fypxfrd"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)
    assert services.returncode == 0

def test_yppasswd():
    services = subprocess.run(["rpcinfo -p server| grep yppasswd"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)
    assert services.returncode == 0
    
def test_nsswitch():
    nsswitch = subprocess.run(["cat /etc/nsswitch.conf | grep nis | grep 'passwd\\|group\\|gshadow\\|shadow\\|netgroup'"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)
    assert nsswitch.returncode == 0

def test_yptest():
    yptest = subprocess.run(['yptest'],shell = True)
    assert yptest.returncode == 1


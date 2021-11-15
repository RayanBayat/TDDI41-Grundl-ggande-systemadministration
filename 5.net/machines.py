import subprocess

def test_IP():
    IP = subprocess.run(['cat /etc/network/interfaces | grep 192.168.1.3'],shell = True)
    assert IP.returncode==0

def test_Network():
    Network = subprocess.run(['cat /etc/network/interfaces | grep 255.255.255.0'],shell = True)
    assert Network.returncode==0

def test_Gateway():
    Gateway = subprocess.run(['cat /etc/network/interfaces | grep 192.168.1.1'],shell = True)
    assert Gateway.returncode==0
    
def test_hostname():
    name = subprocess.run(['cat /etc/hostname | grep server'],shell = True)
    assert name.returncode==0
    
def test_reach_router():
    reaches = subprocess.run(['ping 192.168.1.1 -c 1'],shell = True)
    assert reaches.returncode ==0

test_IP()
test_Network()
test_Gateway()
test_hostname()
test_reach_router()

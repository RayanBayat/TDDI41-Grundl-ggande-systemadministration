import subprocess

def test_named():
    named = subprocess.run(['named-checkconf'],shell = True)

    assert named.returncode ==0

def test_forward():
    forward = subprocess.run(['named-checkzone forward.example.com /etc/bind/forward.example.com | grep OK'],shell = True)

    assert forward.returncode == 0
    
def test_reverse():
    reverse = subprocess.run(['named-checkzone reverse.example.com.in-addr.arpa /etc/bind/reverse.example.com | grep OK'],shell = True)

    assert reverse.returncode == 0
def test_forward_machines_client_1():
    forward = subprocess.run(['nslookup client-1 | grep 192.168.1.2'],shell = True)
    assert forward.returncode == 0
def test_forward_machines_client_2():
    forward = subprocess.run(['nslookup client-2 | grep 192.168.1.4'],shell = True)
    assert forward.returncode == 0
def test_forward_machines_router():
    forward = subprocess.run(['nslookup router | grep 192.168.1.1'],shell = True)
    assert forward.returncode == 0

def test_reverse_machines_client_1():
    reverse = subprocess.run(['nslookup 192.168.1.2 | grep client-1'],shell = True)
    assert reverse.returncode == 0
def test_reverse_machines_client_2():
    reverse = subprocess.run(['nslookup 192.168.1.4 | grep client-2'],shell = True)
    assert reverse.returncode == 0
def test_reverse_machines_router():
    reverse = subprocess.run(['nslookup 192.168.1.1| grep router'],shell = True)
    assert reverse.returncode == 0

test_named()
test_forward()
test_reverse()
test_forward_machines_client_1()
test_forward_machines_client_2()
test_forward_machines_router()
test_reverse_machines_client_1()
test_reverse_machines_client_2()
test_reverse_machines_router()

import subprocess


def test_DNS_server():
    search = subprocess.run(['nslookup google.com | grep Server | grep 192.168.1.3'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell = True)

    assert search.returncode == 0


test_DNS_server()

import subprocess

def test_ping():
    ping = subprocess.run(['ping 10.0.2.2 -c 1'],shell = True)
    assert ping.returncode == 0

def test_ipforwarding():
    # print((subprocess.run(['cat /proc/sys/net/ipv4/ip_forward'],shell = True)))
     if (subprocess.run(['cat /proc/sys/net/ipv4/ip_forward'],shell = True))==1:
        ipforwarding = subprocess.run('true')
        assert ipforwarding.returncode == 0
     else:
        ipforwarding = subprocess.run('false')
        assert ipforwarding.returncode == 1
def test_masquerade():
    masquerade = subprocess.run(['iptables -t nat -L | grep MASQUERADE'],shell = True)
    assert masquerade.returncode == 0
    
    #print(ip_forwarding)





    
test_ping()
test_ipforwarding()
test_masquerade()

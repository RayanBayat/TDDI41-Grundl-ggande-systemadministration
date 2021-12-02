import subprocess
#server = 192.168.1.3
#client-1 = 192.168.1.2
#client-2 = 192.168.1.4

def test_mounted1():
        mounted = subprocess.run(['showmount -e | grep /home1 | grep 192.168.1.2 | grep 192.168.1.4'], shell = True)
        assert mounted.returncode == 0

def test_mounted2():
        mounted = subprocess.run(['showmount -e | grep /home2 | grep 192.168.1.2 | grep 192.168.1.4'], shell = True)
        assert mounted.returncode == 0

def test_mounted3():
        mounted = subprocess.run(['showmount -e | grep /usr/local | grep 192.168.1.2 | grep 192.168.1.4'], shell = True)
        assert mounted.returncode == 0 

def test_flags():
        flags = subprocess.run(['cat /etc/exports | grep rw,sync,root_squash,no_subtree_check'], shell = True)
        assert flags.returncode == 0


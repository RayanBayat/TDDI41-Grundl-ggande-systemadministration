import subprocess 

#def test_conf():
#        conf = subprocess.run(['cat /etc/ntp.conf | grep se.pool.ntp.org'], shell = True)
#        assert conf.returncode == 0

def test_conf():
        conf = subprocess.run(['ntpstat | grep 192.168.1.1'], shell = True)
        assert conf.returncode == 0

def test_queries():
        quer = subprocess.run(['ntpq -p | grep *NTP-server'], shell = True)
        assert quer.returncode == 0

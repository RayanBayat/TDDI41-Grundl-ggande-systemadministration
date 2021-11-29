import subprocess

def test_conf():
        conf = subprocess.run(['cat /etc/ntp.conf | grep se.pool.ntp.org'], shell = True)
        assert conf.returncode == 0
test_conf()

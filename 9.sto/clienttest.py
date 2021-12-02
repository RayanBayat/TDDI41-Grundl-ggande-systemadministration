import subprocess

def test_mounted_usr_local():
        mounted = subprocess.run(['df -h | grep 192.168.1.3:/usr/local'], shell = True)
        assert mounted.returncode == 0

def test_mounted_usr_local1():
        mounted = subprocess.run(["cat /etc/fstab | grep '192.168.1.3:/usr/local /usr/local_client' | grep 'nfs auto,nosuid,nodev,nofail,x-gvfs-show 0 0'"],shell = True)

        assert mounted.returncode == 0

def test_NIS():
        Nis = subprocess.run(["cat /etc/nsswitch.conf | grep automount | grep nis"],shell = True)
        assert Nis.returncode == 0


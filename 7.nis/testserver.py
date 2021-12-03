import subprocess


    
def test_directory1():
    directory = subprocess.run(['ypmatch -x'],shell = True)
    assert directory.returncode == 0

def test_yptest():
    yptest = subprocess.run(['yptest'],shell = True)
    assert yptest.returncode == 1

test_directory1()

import subprocess


    
def test_directory1():
    directory = subprocess.run(['ypmatch -x'],shell = True)
    assert directory.returncode == 0


#test_directory()
test_directory1()

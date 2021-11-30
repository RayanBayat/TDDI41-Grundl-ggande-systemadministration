import subprocess 
import os
import sys
import string



def test_conf():
        conf = subprocess.run(['ntpstat | grep 192.168.1.1'], shell = True)
        assert conf.returncode == 0

def test_queries():
        quer = subprocess.run(['ntpq -p | grep *NTP-server'], shell = True)
        assert quer.returncode == 0
def test_time():
        time = subprocess.run(['ntpstat | grep polling'],shell = True, capture_output=True)        
        word = time.stdout.decode("utf-8")
        words = word.split()
        timer = int(words[3])
        answer = subprocess.run('true')
        if timer >= 64 or timer <= 1024:          
                assert answer.returncode == 0
        else:
                assert answer.returncode == 1
def test_time1():
        time = subprocess.run(['ntpstat | grep time'],shell = True, capture_output=True)        
        word = time.stdout.decode("utf-8")
        words = word.split()
        timer = int(words[4])
        answer = subprocess.run('true')
        if timer >= 0 or timer <= 180000:          
                assert answer.returncode == 0
        else:
                assert answer.returncode == 1
                      
test_conf()
test_queries()
test_time()
test_time1()

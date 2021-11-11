# importing linrary
import os
import subprocess
import sys
import getpass
import secrets
import string
import crypt
import re

def create_username(user_list):
    subprocess.run(['iconv', '-f', 'UTF-7', '-t', 'ASCII', '-c', '-o', 'names_output.txt', 'names.txt'])
    # vi ersätter alla specialbokstäver med motsvarande i ascii och sparar om det i filen
    with open('names_output.txt','r+') as file:
        my_lists = file.readlines()
        
        loop_counter = 0
    
        for x in my_lists:
            person = my_lists[loop_counter].split()
            loop_counter = loop_counter+1
            if len(person) < 1:
                continue
            firstpart = list(''.join(filter(str.isalpha,person[0]))) #vi tar bort alla charactarer som inte är bokstäver
            if len(person) >= 2:
                lastpart = list(''.join(filter(str.isalpha,person[1])))
                if len(firstpart) > 2 and len(lastpart) >= 2:
                    username = firstpart[0]+firstpart[1]+firstpart[2]+lastpart[0]+lastpart[1]+str(loop_counter)
                elif len(lastpart) > 2 and len(firstpart) == 2:
                    username = firstpart[0]+firstpart[1]+lastpart[0]+lastpart[1]+lastpart[2]+str(loop_counter)
                else:
                    username = ''.join((secrets.choice(string.ascii_letters) for i in range(5)))+str(loop_counter)
            else:
                username = ''.join((secrets.choice(string.ascii_letters) for i in range(5)))+str(loop_counter)
            username = username.lower()
            user_list.append(username)
            

def add_user(user_list):
     my_dict = {}
     for x in user_list:
         username = x
         password = ''.join((secrets.choice(string.ascii_letters) for i in range(3)))#ett sätt i python att skapa säkra lösenord som är 3 charactarer långa
         enc_pass = crypt.crypt(password)#vi krypterar lösenordet
         my_dict.update({username:password})# vi sparar lösenordet i mappen framför namnet
     
         try:
             subprocess.run(['useradd', '-p', enc_pass, '-m', username]) # med -p sätter vi lösenordet för användaren och med -m skapar vi home directory för användaren
             print('\x1b[32m'+"User "+ username+ " created" + '\x1b[0m')
         except:
             print('\033[31m' + "Failed to add user.")
             print('\x1b[0m')
             sys.exit(1)
     print("User : " + "Password")  
     for key in my_dict:
         print(key,':',my_dict[key])

def user_delete(user_list):
    print('\x1b[32m')
    for x in user_list:
       
        subprocess.run(['userdel', '-r', x]) 
    print('\x1b[0m')
def test_is_root():
    user = 'root'
    exists = subprocess.run('cat /etc/passwd | grep ' + user,stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT,shell = True)
    #false_cmd = subprocess.run('true')
    assert exists.returncode == 0
    #is_root= os.geteuid()
    #word = 'root'
    #false_cmd = subprocess.run('false')
    #if is_root == 0:
    #    print(is_root)
    #    print("Root exists")
    #    false_cmd = subprocess.run('true')
    #assert false_cmd.returncode == 0

def test_noshell():
    user = 'games'
    exists = subprocess.run('cat /etc/passwd | grep ' + user + '| grep nologin',stdout=subprocess.DEVNULL, #vi tar bort standart utskriftet från terminalen
    stderr=subprocess.STDOUT,shell = True)
    assert exists.returncode == 0

    
# här börjar main funktionen
print('\x1b[33m'+"================================================"+'\x1b[0m')
user_list = []
create_username(user_list)
add_user(user_list)
print('\x1b[32m'+"*^^*^^*All users added*^^*^^*" + '\x1b[0m')
user_delete(user_list)
print('\x1b[32m'+"*__*__*All users deleted*__*__*" + '\x1b[0m')
print('\x1b[33m' + "================================================")
print('\x1b[0m')


test_is_root()
test_noshell()

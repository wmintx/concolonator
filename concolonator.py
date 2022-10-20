################################################################################
#Name: Concolonator
#Author: wmintx
#Concatenates a username, a colon ":", and a password into one string (username:password) per line
#Inputs needed: two text files with only one word per line(username or password)
#Output is a text file named creds.txt.  
#Tested on Python 3.10.7
#
#Nested FOR loops create a list in a file named creds.txt in the following format
#user1:pwd1
#user2:pwd1 
#user3:pwd1
#...
#user1:pwd2
#user2:pwd2
#...
#userN:pwdN
#
#NOTE: Blank lines in either text file will result in a blank username or password 
#   Recommend removing any blank lines; even from the bottom of the list
#Originally designed to be used with Burp Suite Intruder with Base64 processing
##################################################################################

import sys

n = len(sys.argv)
#test for 2 arguments, if missing, gives usage statement
if n < 3:
    print ("Usage: $python3 concolonator.py <Username_file> <Password_file>")
else:
    A = 0
    B = 0
    userlist = sys.argv[1]
    pwdlist = sys.argv[2]
    
    user = open(userlist,'r')
    pwd = open(pwdlist,'r')

    try:
        fp = open('creds.txt', 'x') #checks for prev creds.txt
    except:
        print('File creds.txt already exists in this folder.  Please remove or delete.')
        exit()

    fp = open('creds.txt', 'w') #creates and opens creds.txt
    passlist = pwd.readlines()
    userlist = user.readlines()
    p_len =len(passlist)
    u_len =len(userlist)

    for line in passlist:
        for line in userlist:
            cred=(userlist[A].rstrip() +":"+passlist[B]) #rstrip removes newline
            fp.write(cred)  #writes each string into creds.txt
            A+=1
            #Test if userlist indexer value A is larger than userlist length, if yes,break out
            if A == u_len + 1:
                break
        B+=1
        A=0
        #Test if passlist indexer value B is larger than passlist length, if yes,break out
        if B == p_len +1:
            break
    fp.close()
    user.close()
    pwd.close()

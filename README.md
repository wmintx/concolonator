################################################################################
Name: Concolonator
Description: Concatenates a username or any word, a colon ":", and a password or any other word into one string (username:password) per line
Usage: $python3 concolonator.py <usernames.txt> <passwords.txt>
Inputs needed: two text files with only one word per line (e.g., username or password)
Output is a text file named creds.txt

NOTE1: Script checks for a current "creds.txt" file and will error out until it is renamed or removed.
NOTE2: Blank lines in either text file will result in a blank username or password 
   Recommend removing any blank lines; even from the bottom of the list

Tested on Python 3.10.7

Creates a list in a file named creds.txt in the following format
user1:pwd1
user2:pwd1 
user3:pwd1
...
user1:pwd2
user2:pwd2
...
user1:pwdN
user2:pwdN

Originally designed to be used with Burp Suite Intruder with Base64 processing
##################################################################################

import imaplib, re
import os
import time
import socket

imap_host = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_host)
password = open('password.txt','r')
password = password.read()
mail.login("hmurraydavis@gmail.com", password)
mail.select("inbox") # connect to inbox.

result, data = mail.uid('search', None, 'UNSEEN')
uid_list = data[0].split()
print len(uid_list), 'Unseen emails.'


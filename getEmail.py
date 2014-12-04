import imaplib, re
import os
import time
import socket
import email
 
imap_host = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_host)
password = open('password.txt','r')
password = password.read()
mail.login("messagespectrum@gmail.com", password)
mail.select("inbox") # connect to inbox.
 
def get_mail(mail):
    result, data = mail.uid('search', None, 'UNSEEN')
    uid_list = data[0].split()
    print len(uid_list), 'Unseen emails.'
 
    mails = []
 
    for messageID in uid_list:
        result, data = mail.fetch(messageID, "(RFC822)") # fetch the email body (RFC822) for the given ID
        raw_email = data[0][1] # here's the body, which is raw text of the whole email
        #print raw_email
        email_message = email.message_from_string(raw_email)
 
        bodytext=email_message.get_payload()[0].get_payload()
        if type(bodytext) is list:
            bodytext=','.join(str(v) for v in bodytext)
 
        mails.append({'from': email_message['From'], 'body': bodytext})
 
    return mails
 
print get_mail(mail)

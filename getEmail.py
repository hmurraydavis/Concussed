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

result, data = mail.uid('search', None, 'UNSEEN')
uid_list = data[0].split()
print len(uid_list), 'Unseen emails.'
print 'uid a:', uid_list[0]

for messageID in uid_list:
    result, data = mail.fetch(messageID, "(RFC822)") # fetch the email body (RFC822) for the given ID
    raw_email = data # here's the body, which is raw text of the whole email
    print raw_email


#email_message = email.message_from_string(raw_email)
# 
#print 'to', email_message['To']
# 
#print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>
# 
#print email_message.items() # print all headers
# 
## note that if you want to get text content (body) and the email contains
## multiple payloads (plaintext/ html), you must parse each message separately.
## use something like the following: (taken from a stackoverflow post)
#def get_first_text_block(self, email_message_instance):
#    maintype = email_message_instance.get_content_maintype()
#    if maintype == 'multipart':
#        for part in email_message_instance.get_payload():
#            if part.get_content_maintype() == 'text':
#                return part.get_payload()
#    elif maintype == 'text':
#        return email_message_instance.get_payload()

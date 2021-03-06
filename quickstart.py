#!/usr/bin/python

import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run
import base64
import email
from apiclient import errors


# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = 'client_secret.json'
#CLIENT_SECRET_FILE = '~/Downloads/client_secret_624504023137-rljeqvc09tmptkpqpmqtbs16ij9emkns.apps.googleusercontent.com.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  credentials = run(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

# Retrieve a page of threads
threads = gmail_service.users().threads().list(userId='me').execute()

# Print ID for each thread
if threads['threads']:
  for thread in threads['threads']:
    print 'Thread ID: %s' % (thread['id'])
    message = gmail_service.users().messages().get(userId='hmurraydavis@gmail.com',
    id=thread['id'], format='raw').execute()
    print message
    
if __name__=='__main__':
    print 'hi'
#    ListMessagesWithLabels()

from __future__ import print_function
import email

import imaplib
from nltk.tokenize import sent_tokenize 
import datetime
from oauth2client import file, client, tools
from apiclient.discovery import build
from apiclient import discovery

#######
######
######
# code to write in the google sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials


from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import httplib2
import os
from apiclient import errors

from apiclient.discovery import build
from apiclient import discovery


#try:
#    import argparse
#    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
#except ImportError:
#    flags = None
#
## use creds to create a client to interact with the Google Drive API
#scope = ['https://spreadsheets.google.com/feeds']
#credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#gc = gspread.authorize(credentials)
#sht1 = gc.open_by_key('1DSDsofRleKMODoAWQNJf5wnr4sNgHXZ-1Jq9XbiEgYw').sheet1
#
## Extract and print all of the values
#list_of_hashes = sht1.get_all_records()
#print(list_of_hashes)

# Extract and print all of the values
#sht1.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")

username = 'aditya.tripathi@iitgn.ac.in'
password= 'awpzrymt'
mail=imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username,password)
mail.select('inbox')
mail.list()
result,data=mail.uid('search',None,'ALL')
inbox_item_list=data[0].split()
mails=inbox_item_list[-7]
result2,email_data=mail.uid('fetch',mails,'(RFC822)')
raw_email=email_data[0][1].decode('utf-8')
html_of_current_mail=raw_email
import mailparser
mail = mailparser.parse_from_string(raw_email)
s1=''
s='--- mail_boundary ---'
for i in range(len(mail.body)-len(s)+1):
    if mail.body[i:i+len(s)]==s:
        break
    s1+=mail.body[i]

s2=''
for i in s1.split():
    s2+=i+' '
#print(s2)


import base64
    from apiclient import errors


    def GetAttachments(service, user_id, msg_id, prefix=""):
       """Get and store attachment from Message with given id.

       Args:
       service: Authorized Gmail API service instance.
       user_id: User's email address. The special value "me"
       can be used to indicate the authenticated user.
       msg_id: ID of Message containing attachment.
       prefix: prefix which is added to the attachment filename on saving
       """
       try:
           message = service.users().messages().get(userId=user_id, id=msg_id).execute()

           for part in message['payload'].get('parts', ''):
              if part['filename']:
                  if 'data' in part['body']:
                     data=part['body']['data']
                  else:
                     att_id=part['body']['attachmentId']
                     att=service.users().messages().attachments().get(userId=user_id, messageId=msg_id,id=att_id).execute()
                     data=att['data']
            file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
            path = prefix+part['filename']

            with open(path, 'wb') as f:
                f.write(file_data)

        except errors.HttpError as error:
            print('An error occurred: %s' % error)
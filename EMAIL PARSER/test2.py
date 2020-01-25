from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import httplib2
import os
from apiclient import errors

from apiclient.discovery import build
from apiclient import discovery


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None





CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Quickstart'


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
# def main():
    
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))


def ListMessagesMatchingQuery(service, user_id, query):

    try:
        response = service.users().messages().list(userId=user_id,
                                                   q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,
                                             pageToken=page_token).execute()
            messages.extend(response['messages'])

        return(messages)
        
    except(errors.HttpError):
        print('An error occurred:')





messages = ListMessagesMatchingQuery(service,'me',query='label:parser_test')
print(messages)
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
              if part['a']:
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
GetAttachments(service,'me',)
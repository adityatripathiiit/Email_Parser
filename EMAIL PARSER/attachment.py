import imaplib, email, os

user = 'aditya.tripathi@iitgn.ac.in'
password = 'awpzrymt'
imap_url = 'imap.gmail.com'
#Where you want your attachments to be saved (ensure this directory exists) 
attachment_dir = r'C:\Users\Aditya Tripathi\Desktop\Email parsing\Devrrat'
g = geocoder.ip('me')
m=g.latlng
q=socket.gethostbyname(socket.gethostname())
mail=imaplib.IMAP4_SSL('imap.gmail.com')
try:
    mail.login(username,password)
except Exception:
    log_in(username,password)
    time.sleep(4)
mail.select('inbox')
mail.list(username,password)
result,data=mail.uid('search',None,'ALL')
inbox_item_list=data[0].split()
for j in range(k):
    mails=inbox_item_list[len(inbox_item_list)-1-j]
    result2,email_data=mail.uid('fetch',mails,'(RFC822)')
    raw_email=email_data[0][1].decode('utf-8')
    email_message=email.message_from_string(raw_email)



# sets up the auth
def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con
# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
# allows you to download attachments
def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype()=='multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))
#search for a particular email
def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data
#extracts emails from byte array
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

con = auth(user,password,imap_url)
con.select('INBOX')

result, data = con.fetch(b'10','(RFC822)')
raw = email.message_from_bytes(data[0][-1])
get_attachments(raw)
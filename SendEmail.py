import smtplib

GMAIL_USER = ''
GMAIL_PASS = ''
SMTP_SERVER = ''
SMTP_PORT = ''

def Send_Email (recipient, subject, text):
smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(GMAIL_USER, GMAIL_PASS)
header = 'To: ' + recipient + '\n' + 'From: ' + GMAIL_USER
header = header + '\n' + 'Subject:' + subject + '\n'
msg = header + '\n' + text + '\n\n'
smtpserver.sendmail(GMAIL_USER, recipient, msg)
smtpserver.close()

#call Send_Email with params
# Send_Email('DestoEmailAddress', 'Subjectfield','Message text')
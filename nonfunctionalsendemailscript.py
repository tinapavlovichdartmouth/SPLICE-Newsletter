#! /usr/local/bin/python


SMTPserver = 'smtp.mail.me.com'
sender =     'tina.pavlovich@dartmouth.edu'
destination = ['f0051sz@dartmouth.edu']

USERNAME = input("Give me your username:")
PASSWORD = input("Now your password!!")

# typical values for text_subtype are plain, html, xml
text_subtype = 'html'


content=open("splice-newsletter-86.html", "r")
email_text=content.read()

subject="test"

import sys

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

try:
    msg = MIMEText(email_text, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all
    
    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()
        
except:
    sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message
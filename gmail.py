# -*- coding: utf-8 -*-
from imapclient import IMAPClient
import email
import smtplib, ssl
from summary import summary
from time import sleep
import configparser
import datetime

config = configparser.ConfigParser()
config.read('config.ini')

id = config['default']['username']
password = config['default']['password']

# context manager ensures the session is cleaned up
ssl_context = ssl.create_default_context()

# don't check if certificate hostname doesn't match target hostname
ssl_context.check_hostname = False

# don't check if the certificate is trusted by a certificate authority
ssl_context.verify_mode = ssl.CERT_NONE

def sendmail(to, title, body, inreply="new"):
    sum_body =  summary(body)
    message = "Subject: " + title + \
        "\nIn-Reply-To: " + inreply + \
        "\nFrom: Auto Summary <autosumkr@gmail.com>" + \
        "\n\n" + sum_body + "\n---\n" + body

    with smtplib.SMTP_SSL("smtp.gmail.com", context=ssl_context) as server:
        server.login(id, password)
        server.sendmail(id, to, message.encode("utf8"))


def check_imap():
    with IMAPClient(host="imap.gmail.com", ssl_context=ssl_context) as client:
        client.login(id, password)
        client.select_folder('INBOX')

        # search criteria are passed in a straightforward way
        # (nesting is supported)
        messages = client.search(['NOT', 'DELETED'])

        # fetch selectors are passed as a simple list of strings.
        response = client.fetch(messages, ['FLAGS', 'RFC822'])

        # `response` is keyed by message id and contains parsed,
        # converted response items.
        for message_id, data in response.items():
            email_message = email.message_from_bytes(data[b"RFC822"])
            efrom = email_message.get("From")
            eto = email_message.get("To")
            esubject = email_message.get("Subject")
            inreply = email_message.get("Message-ID")

            if eto == "autosumkr@gmail.com":
                mailto = efrom
            else:
                mailto = eto
            
            ebody = ""
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    charset = part.get_content_charset()
                    ebody = str(part.get_payload(decode=True), 'utf-8', 'ignore')
            
            sendmail(mailto, esubject, ebody, inreply)
            client.delete_messages(message_id)
            print("Sent", mailto, message_id, inreply, esubject)
        client.expunge()
        client.logout()

if __name__ == "__main__":
    while(not sleep(60)):
        print("Checking again at", datetime.datetime.now())
        check_imap()


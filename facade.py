# -*- coding: utf-8 -*-
import smtplib
import imaplib


class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        from_email = f'{self.username}@{self.host}' if '@' not in self.username else self.username
        message = (f'From {from_email} \r\n' f'To:{to_email}\r\n Subject:{subject}\r\n\r\n{message}')
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_addr=from_email, to_addrs=[to_email], msg=message)

    def get_inbox(self): #?
        mailbox = imaplib.IMAP4(host=self.host)
        mailbox.login(bytes(string=self.username, encoding="utf8"), bytes(string=self.password, encoding="utf-8"))
        mailbox.select(mailbox='INBOX')
        x, data = mailbox.search(charset=None, criteria="ALL")
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(message_set=num,message_parts="(RFC822)")
            messages.append(message[0][1])

        return messages

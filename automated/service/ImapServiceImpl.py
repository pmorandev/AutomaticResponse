from email.message import Message
from automated.model.Email import Email
from typing import List
from automated.service.Service import Service
from bs4 import BeautifulSoup
import imaplib
import email
 
class ImapServiceImpl(Service):

    UNREAD_EMAIL_CODE_SEARCH = "(UNSEEN)"
    FETCH_DATA_MESSAGE_CODE = "(RFC822)"
    EMAIL_FROM_CODE = "from"
    EMAIL_SUBJBECT_CODE = "subject"
    IMAP_RESPONSE_CODE_OK = "OK"
    EMAIL_CONTENT_TYPE_TEXT = "text/plain"
    EMAIL_CONTENT_TYPE_HTML = "text/html"
    SERVER_IMAP_INDEX =0
    USER_IMAP_INDEX = 1
    PASS_IMAP_INDEX = 2
    EMAIL_CONTENT_INDEX = 1

    def __init__(self, arg, source = None) -> None:
        try:
            self.source = source or self.builtSource(arg)
            super().__init__(source)
        except imaplib.IMAP4.error:
            raise

    def builtSource(self, arg):
        try:
            emailServer = imaplib.IMAP4_SSL(arg[self.SERVER_IMAP_INDEX])
            emailServer.login(user=arg[self.USER_IMAP_INDEX], password=arg[self.PASS_IMAP_INDEX])
            return emailServer
        except imaplib.IMAP4.error:
            raise

    def getEmailIds(self, emails):
        emailIds = []
        for data in emails:
            emailIds += data.split()
        return emailIds

    def getBodyFromEmailContent(self, content: Message):
        if content.is_multipart():
            body = ''
            for part in content.get_payload():
                if part.get_content_type() == self.EMAIL_CONTENT_TYPE_TEXT:
                    body += part.get_payload(decode=True).decode()
                elif part.get_content_type() == self.EMAIL_CONTENT_TYPE_HTML:
                    soup = BeautifulSoup(markup=part.get_payload(decode=True).decode(), features="html.parser")
                    body += soup.get_text()
            return body
        else:
            return content.get_payload()

    def getEmailData(self, idEmail):
        (responseCode, data) = self.source.fetch(idEmail, self.FETCH_DATA_MESSAGE_CODE)
        if responseCode == self.IMAP_RESPONSE_CODE_OK:
            fromSource, subject, body  = '', '', ''
            for content in data:
                if isinstance(content, tuple):
                    content = email.message_from_bytes(content[self.EMAIL_CONTENT_INDEX])
                    fromSource = content[self.EMAIL_FROM_CODE]
                    subject = content[self.EMAIL_SUBJBECT_CODE]
                    body = self.getBodyFromEmailContent(content)
            return Email(subject, body, fromSource)
        else:
            return None
        
    def searchEmailsFromServer(self, codeEmailSearch):
        self.source.select(readonly=True)
        (responseCode, emails) = self.source.search(None, codeEmailSearch)
        if responseCode == self.IMAP_RESPONSE_CODE_OK:
            return emails
        else:
            return None
    
    def getNewEmails(self) -> List[Email]:
        emailsMatch = []
        newEmails = self.searchEmailsFromServer(self.UNREAD_EMAIL_CODE_SEARCH)
        emailIds = self.getEmailIds(newEmails)
        if emailIds != None:
            for index in emailIds:
                emailsMatch.append(self.getEmailData(index))
        return emailsMatch
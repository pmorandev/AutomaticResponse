from automated.operation.Operation import Operation
from automated.service.Service import Service
from automated.model.Email import Email
import json
from types import SimpleNamespace
from pathlib import Path
from typing import List
from unittest import TestCase, mock

class testOperation(TestCase):

    base_path = Path(__file__).parent

    def getDataFromJsonFile(self, jsonMockFile: str) -> any:
        file_path = (self.base_path / "../mock/{0}.json".format(jsonMockFile)).resolve()
        with open(file_path,'r') as file:
            data = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
        return data

    def getMockEmails(self) -> List[Email] :
        return self.getDataFromJsonFile("emails")

    def test_getNewEmailsBySubjectMatch(self):
        service = mock.create_autospec(Service)
        service.getNewEmails.return_value = self.getMockEmails()
        operation = Operation(service)
        response = operation.findNewEmails(pattern='NET Core', bySubject= True)
        self.assertEquals(response.responses[0], 'You have 2 New Message(s) with "NET Core" subject')
        self.assertEquals(len(response.responses[1]), 2)

    def test_getNewEmailsBySubjectNoMatch(self):
        service = mock.create_autospec(Service)
        service.getNewEmails.return_value = self.getMockEmails()
        operation = Operation(service)
        response = operation.findNewEmails(pattern='NOT FOUND', bySubject= True)
        self.assertEquals(response.responses[0], 'You have 0 New Message(s) with "NOT FOUND" subject')
        self.assertEquals(len(response.responses[1]), 0)

    def test_NotNewEmailsFound(self):
        service = mock.create_autospec(Service)
        service.getNewEmails.return_value = []
        operation = Operation(service)
        response = operation.findNewEmails(pattern='NOT FOUND', bySubject= True)
        self.assertEquals(response.responses[0], "You don't have New Messages in your inbox")
        self.assertEquals(len(response.responses[1]), 0)
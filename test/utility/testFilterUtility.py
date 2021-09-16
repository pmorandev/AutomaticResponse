import json
from re import I
from types import SimpleNamespace
from automated.model.Filter import Filter
from automated.utility.FilterUtility import FilterUtility
from pathlib import Path
from unittest import TestCase


class testFilterUtility(TestCase):

    base_path = Path(__file__).parent

    def getDataFromJsonFile(self, jsonMockFile: str) -> any:
        file_path = (self.base_path / "../mock/{0}.json".format(jsonMockFile)).resolve()
        with open(file_path,'r') as file:
            data = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))
        return data

    def createFilterMock(self, pattern) -> Filter:
        return Filter("test", pattern)

    def getMockEmails(self) :
        return self.getDataFromJsonFile("emails")

    def test_findNetJobsEmailsByBody(self):
        netJobFilter = self.createFilterMock("NET Core")
        emails = self.getMockEmails()
        filter = FilterUtility()
        emailsMatch = filter.getEmailsMatchByBody(emails, netJobFilter)
        self.assertEqual(len(emailsMatch), 2)
        self.assertEqual(emailsMatch[0].fromSource, "deepakk@caspex.com")
        self.assertEqual(emailsMatch[1].fromSource, "amit.singh@diverselynx.com")

    def test_findJavaJobsEmailsByBody(self):
        netJobFilter = self.createFilterMock("Java")
        emails = self.getMockEmails()
        filter = FilterUtility()
        emailsMatch = filter.getEmailsMatchByBody(emails, netJobFilter)
        self.assertEqual(len(emailsMatch), 2)
        self.assertEqual(emailsMatch[0].fromSource, "shree@emonics.com")
        self.assertEqual(emailsMatch[1].fromSource, "nsullivan@diversant.com")

    def test_findNetJobsEmailsBySubject(self):
        netJobFilter = self.createFilterMock("NET Core")
        emails = self.getMockEmails()
        filter = FilterUtility()
        emailsMatch = filter.getEmailsMatchBySubject(emails, netJobFilter)
        self.assertEqual(len(emailsMatch), 2)

    def test_findJavaJobsEmailsBySubject(self):
        netJobFilter = self.createFilterMock("Java")
        emails = self.getMockEmails()
        filter = FilterUtility()
        emailsMatch = filter.getEmailsMatchBySubject(emails, netJobFilter)
        self.assertEqual(len(emailsMatch), 2)
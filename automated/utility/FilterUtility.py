
from typing import List
from automated.model.Filter import Filter
from automated.model.Email import Email
import re


class FilterUtility:

    def matchContent(self, content: str, pattern: str) -> bool:
        return (re.search(pattern, content) != None) or False

    def getEmailsMatchByBody(self, emails: List[Email], filter: Filter) -> List[Email]:
        emailsMatch = []
        for email in emails:
            if self.matchContent(email.body, filter.pattern) : emailsMatch.append(email)
        return emailsMatch

    def getEmailsMatchBySubject(self, emails: List[Email], filter: Filter) -> List[Email]:
        emailsMatch = []
        for email in emails:
            if self.matchContent(email.subject, filter.pattern) : emailsMatch.append(email)
        return emailsMatch

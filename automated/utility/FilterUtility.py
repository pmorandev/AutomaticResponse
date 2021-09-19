
from typing import List
from automated.model.Pattern import Pattern
from automated.model.Email import Email
import re


class FilterUtility:

    def matchContent(self, content: str, pattern: str) -> bool:
        return (re.search(pattern, content) != None) or False

    def getEmailsMatchByBody(self, emails: List[Email], pattern: Pattern) -> List[Email]:
        emailsMatch = []
        for email in emails:
            if self.matchContent(email.body, pattern.pattern) : emailsMatch.append(email)
        return emailsMatch

    def getEmailsMatchBySubject(self, emails: List[Email], pattern: Pattern) -> List[Email]:
        emailsMatch = []
        for email in emails:
            if self.matchContent(email.subject, pattern.pattern) : emailsMatch.append(email)
        return emailsMatch

from typing import List
from automated.model.Email import Email


class Service:

    def __init__(self, source) -> None:
        self.source = source

    def builtSource(self, arg):
        pass

    def getNewEmails(self) -> List[Email]:
        pass

    def getEmailsByFrom(self, fromSource: str) -> List[Email]:
        pass
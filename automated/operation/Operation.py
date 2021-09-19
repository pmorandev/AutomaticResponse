from automated.utility.FilterUtility import FilterUtility
from automated.model.Pattern import Pattern
from automated.operation.Response import Response
from automated.service.Service import Service

class Operation(object):

    def __init__(self, service: Service) -> None:
        self.emailService = service
        super().__init__()

    def findNewEmails(self, pattern: str, bySubject: bool = True) -> Response:
        try:
            responses = []
            emails = self.emailService.getNewEmails()
            if len(emails) > 0:
                applicablePattern = Pattern("", pattern)
                filter = FilterUtility()
                matchingEmails = filter.getEmailsMatchBySubject(emails, applicablePattern)
                responses.append('You have {0} New Message(s) with "{1}" {2}'.format(
                    len(matchingEmails), pattern, ('subject' if bySubject else 'body')))
                responses.append(matchingEmails)
            else:
                responses.append("You don't have New Messages in your inbox")
                responses.append(emails)
            return Response(True, responses, None)
        except RuntimeError as ex:
            return Response(False, None, ex.args)

class Email(object):

    def __init__(self, subject: str, body: str, fromSource: str) -> None:
        self.subject = subject
        self.body = body
        self.fromSource = fromSource
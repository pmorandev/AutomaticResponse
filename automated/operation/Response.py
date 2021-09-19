
from typing import List

class Response:

    def __init__(self, success: bool, responses: List, error: any) -> None:
        self.success = success
        self.responses = responses
        self.error = error
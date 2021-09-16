
from typing import Pattern


class Filter(object):

    def __init__(self, name: str, pattern: str) -> None:
        self.pattern =pattern
        self.name = name
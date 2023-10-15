from __future__ import annotations

from typing import Iterable, TextIO


class TokenizerError(Exception):
    pass


class Token:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<{self.name}>"


# keywords
SWAP = Token("swap")
DUP = Token("dup")
DROP = Token("drop")

# operators
ADD = Token("+")
SUB = Token("-")
MUL = Token("*")

EQUALS = Token("=")
LESS_THAN = Token("<")
GREATER_THAN = Token(">")
NOT = Token("!")

TOKEN_MAP = {
    "swap": SWAP,
    "dup": DUP,
    "drop": DROP,
    "+": ADD,
    "-": SUB,
    "*": MUL,
    "=": EQUALS,
    "<": LESS_THAN,
    ">": GREATER_THAN,
    "!": NOT,
}


class Literal(Token):
    value: int
    name: str = "literal"

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"<{self.name}: {self.value}>"


def parse_token(s: str, l: int, t: int) -> Token:
    s = s.lower()
    if s in TOKEN_MAP:
        return TOKEN_MAP[s]
    try:
        return Literal(int(s))
    except ValueError:
        raise TokenizerError(f"{l}:{t} invalid token: {s}")


def tokenize(s: TextIO) -> Iterable[Token]:
    for l, line in enumerate(s):
        line = line.split("#")[0]
        for t, token in enumerate(line.split()):
            if not token:
                continue
            yield parse_token(token, l, t)

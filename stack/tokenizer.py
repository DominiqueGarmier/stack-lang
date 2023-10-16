from __future__ import annotations

from collections.abc import Iterable
from typing import TextIO

from .excs import TokenizerError


class Token:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<{self.name}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Token):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


# keywords
SWAP = Token("SWAP")
DUP = Token("DUP")
DROP = Token("DROP")
APPLY = Token("APPLY")

LOAD = Token("LOAD")
STORE = Token("STORE")

ADD = Token("+")
SUB = Token("-")
MUL = Token("*")

EQUALS = Token("=")
LESS_THAN = Token("<")
GREATER_THAN = Token(">")

NOT = Token("!")
AND = Token("&")
OR = Token("|")
XOR = Token("^")

L_BRACKET = Token("[")
R_BRACKET = Token("]")


TOKEN_MAP = {
    "SWAP": SWAP,
    "DUP": DUP,
    "DROP": DROP,
    "APPLY": APPLY,
    # store/load
    "LOAD": LOAD,
    "STORE": STORE,
    # binary operators
    "+": ADD,
    "-": SUB,
    "*": MUL,
    # comparison operators
    "=": EQUALS,
    "<": LESS_THAN,
    ">": GREATER_THAN,
    # boolean operators
    "!": NOT,
    "&": AND,
    "|": OR,
    "^": XOR,
    # brackets
    "[": L_BRACKET,
    "]": R_BRACKET,
}


class Literal(Token):
    value: int
    name: str = "literal"

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"<{self.name}: {self.value}>"


def parse_token(s: str, line_number: int, token_index: int) -> Token:
    s = s.upper()
    if s in TOKEN_MAP:
        return TOKEN_MAP[s]
    try:
        return Literal(int(s))
    except ValueError:
        raise TokenizerError(f"{line_number}:{token_index} invalid token: {s}")


def tokenize(s: TextIO) -> Iterable[Token]:
    for line_number, line in enumerate(s):
        line = line.split("#")[0]
        for token_index, token in enumerate(line.split()):
            if not token:
                continue
            yield parse_token(token, line_number, token_index)

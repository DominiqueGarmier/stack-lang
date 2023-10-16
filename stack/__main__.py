from __future__ import annotations

import sys
from typing import TextIO

from . import interpreter
from . import parser
from . import tokenizer


MAX_EXPR = 2048


def run(src: TextIO) -> int:
    tokens = tokenizer.tokenize(src)
    exprs = parser.parse(tokens)
    stack = interpreter.interpret(exprs, max_counter=MAX_EXPR)

    print(" ".join(repr(expr) for expr in stack))

    return 0


def main() -> int:
    return run(sys.stdin)


if __name__ == "__main__":
    raise SystemExit(main())

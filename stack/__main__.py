from __future__ import annotations

import sys
from . import tokenizer
from . import interpreter
from . import parser

MAX_EXPR = 2048


def main() -> int:
    tokens = tokenizer.tokenize(sys.stdin)
    exprs = parser.parse(tokens)
    stack = interpreter.interpret(exprs, max_counter=MAX_EXPR)

    print(" ".join(repr(expr) for expr in stack))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

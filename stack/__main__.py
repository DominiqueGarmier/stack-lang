from __future__ import annotations

import sys
from . import tokenizer
from . import interpreter


def main() -> int:
    tokens = tokenizer.tokenize(sys.stdin)
    stack = interpreter.interpret(tokens)
    for token in stack:
        print(repr(token))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

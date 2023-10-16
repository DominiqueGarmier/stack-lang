from __future__ import annotations

import sys

from stack.run import run


def main() -> int:
    return run(sys.stdin)


if __name__ == "__main__":
    raise SystemExit(main())

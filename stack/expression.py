from __future__ import annotations


class Expression:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"<{self.name}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Expression):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Literal(Expression):
    name: str = "LITERAL"
    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"<{self.name} {self.value}>"


class Lambda(Expression):
    name: str = "LAMBDA"
    nested: list[Expression]

    def __init__(self, nested: list[Expression]) -> None:
        self.nested = nested

    def __repr__(self) -> str:
        return f"<{self.name} [ {' '.join([repr(n) for n in self.nested])} ]>"

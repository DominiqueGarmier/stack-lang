from __future__ import annotations
from re import A

from typing import Iterable, TypeGuard

from . import tokenizer
from .tokenizer import Token, Literal


class InterpreterError(Exception):
    pass


def assert_literal(t: Token) -> TypeGuard[Literal]:
    if not isinstance(t, Literal):
        raise InterpreterError(f"Expected literal, got {t}")
    return True


def _op_SWAP(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()
    stack.append(a)
    stack.append(b)


def _op_DUP(stack: list[Token]) -> None:
    a = stack.pop()
    stack.append(a)
    stack.append(a)


def _op_DROP(stack: list[Token]) -> None:
    stack.pop()


def _op_ADD(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()

    if assert_literal(a) and assert_literal(b):
        stack.append(Literal(a.value + b.value))


def _op_SUB(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()

    if assert_literal(a) and assert_literal(b):
        stack.append(Literal(a.value - b.value))


def _op_MUL(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()

    if assert_literal(a) and assert_literal(b):
        stack.append(Literal(a.value * b.value))


def _op_EQUALS(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()

    if assert_literal(a) and assert_literal(b):
        stack.append(Literal(int(a.value == b.value)))


def _op_LESS_THAN(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()

    if assert_literal(a) and assert_literal(b):
        stack.append(Literal(int(a.value < b.value)))


def _op_GREATER_THAN(stack: list[Token]) -> None:
    a = stack.pop()
    b = stack.pop()

    if assert_literal(a) and assert_literal(b):
        stack.append(Literal(int(a.value > b.value)))


def _op_NOT(stack: list[Token]) -> None:
    a = stack.pop()

    if assert_literal(a):
        stack.append(Literal(int(not a.value)))


def apply_token(
    stack: list[tokenizer.Token], token: tokenizer.Token
) -> list[tokenizer.Token]:
    if token is tokenizer.SWAP:
        _op_SWAP(stack)
    elif token is tokenizer.DROP:
        _op_DROP(stack)
    elif token is tokenizer.DUP:
        _op_DUP(stack)
    elif token is tokenizer.ADD:
        _op_ADD(stack)
    elif token is tokenizer.SUB:
        _op_SUB(stack)
    elif token is tokenizer.MUL:
        _op_MUL(stack)
    elif token is tokenizer.EQUALS:
        _op_EQUALS(stack)
    elif token is tokenizer.LESS_THAN:
        _op_LESS_THAN(stack)
    elif token is tokenizer.GREATER_THAN:
        _op_GREATER_THAN(stack)
    elif token is tokenizer.NOT:
        _op_NOT(stack)
    elif isinstance(token, Literal):
        stack.append(token)
    else:
        raise InterpreterError(f"Unknown token: {token}")

    return stack


def interpret(tokens: Iterable[tokenizer.Token]) -> list[tokenizer.Token]:
    stack = []
    for token in tokens:
        stack = apply_token(stack, token)

    return stack

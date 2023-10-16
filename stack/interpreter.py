from __future__ import annotations

from typing import Iterable

from . import parser
from .expression import Expression, Literal, Lambda
from . import _ops
from .exceptions import InterpreterError


def apply_token(
    stack: list[Expression], registry: dict[int, Expression], expr: Expression
) -> tuple[list[Expression], dict[int, Expression], list[Expression]]:
    ret: list[Expression] = []

    if expr is parser.SWAP:
        _ops.op_SWAP(stack)
    elif expr is parser.DROP:
        _ops.op_DROP(stack)
    elif expr is parser.DUP:
        _ops.op_DUP(stack)
    elif expr is parser.APPLY:
        ret = _ops.op_APPLY(stack)

    elif expr is parser.LOAD:
        _ops.op_LOAD(stack, registry)
    elif expr is parser.STORE:
        _ops.op_STORE(stack, registry)

    elif expr is parser.ADD:
        _ops.op_ADD(stack)
    elif expr is parser.SUB:
        _ops.op_SUB(stack)
    elif expr is parser.MUL:
        _ops.op_MUL(stack)

    elif expr is parser.EQUALS:
        _ops.op_EQUALS(stack)
    elif expr is parser.LESS_THAN:
        _ops.op_LESS_THAN(stack)
    elif expr is parser.GREATER_THAN:
        _ops.op_GREATER_THAN(stack)

    elif expr is parser.NOT:
        _ops.op_NOT(stack)
    elif expr is parser.AND:
        _ops.op_AND(stack)
    elif expr is parser.OR:
        _ops.op_OR(stack)
    elif expr is parser.XOR:
        _ops.op_XOR(stack)

    elif isinstance(expr, Literal):
        stack.append(expr)
    elif isinstance(expr, Lambda):
        stack.append(expr)
    else:
        raise InterpreterError(f"Unknown expression: {expr}")

    return stack, registry, ret


def interpret(exprs: Iterable[Expression], max_expr: int) -> list[Expression]:
    expr_count: int = 0
    iter_exprs = iter(exprs)

    exprs_stack: list[Expression] = []
    registry: dict[int, Expression] = {}
    stack: list[Expression] = []
    while True:
        try:
            if not exprs_stack:
                exprs_stack = [next(iter_exprs)]
        except StopIteration:
            break

        while exprs_stack:

            if expr_count > max_expr:
                return stack

            expr = exprs_stack.pop()
            stack, registry, callback = apply_token(stack, registry, expr)
            expr_count += 1

            if callback:
                callback = callback.copy()
                callback.reverse()
                exprs_stack.extend(callback)

    return stack

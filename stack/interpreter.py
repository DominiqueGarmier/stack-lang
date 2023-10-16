from __future__ import annotations

from collections.abc import Iterable

from . import ops
from . import parser
from .excs import InterpreterError
from .expr import Expression
from .expr import Lambda
from .expr import Literal


def apply_token(
    stack: list[Expression], registry: dict[int, Expression], expr: Expression
) -> tuple[list[Expression], dict[int, Expression], list[Expression]]:
    ret: list[Expression] = []

    if expr is parser.SWAP:
        ops.op_SWAP(stack)
    elif expr is parser.DROP:
        ops.op_DROP(stack)
    elif expr is parser.DUP:
        ops.op_DUP(stack)
    elif expr is parser.APPLY:
        ret = ops.op_APPLY(stack)

    elif expr is parser.LOAD:
        ops.op_LOAD(stack, registry)
    elif expr is parser.STORE:
        ops.op_STORE(stack, registry)

    elif expr is parser.ADD:
        ops.op_ADD(stack)
    elif expr is parser.SUB:
        ops.op_SUB(stack)
    elif expr is parser.MUL:
        ops.op_MUL(stack)

    elif expr is parser.EQUALS:
        ops.op_EQUALS(stack)
    elif expr is parser.LESS_THAN:
        ops.op_LESS_THAN(stack)
    elif expr is parser.GREATER_THAN:
        ops.op_GREATER_THAN(stack)

    elif expr is parser.NOT:
        ops.op_NOT(stack)
    elif expr is parser.AND:
        ops.op_AND(stack)
    elif expr is parser.OR:
        ops.op_OR(stack)
    elif expr is parser.XOR:
        ops.op_XOR(stack)

    elif isinstance(expr, Literal):
        stack.append(expr)
    elif isinstance(expr, Lambda):
        stack.append(expr)
    else:
        raise InterpreterError(f"Unknown expression: {expr}")

    return stack, registry, ret


def interpret(
    exprs: Iterable[Expression], max_counter: int | None = None
) -> list[Expression]:
    iter_exprs = iter(exprs)
    expression_stack: list[Expression] = []

    registry: dict[int, Expression] = {}
    stack: list[Expression] = []

    counter: int = 0
    while max_counter is None or counter < max_counter:
        if max_counter is not None:
            counter += 1

        try:
            if not expression_stack:
                expression_stack = [next(iter_exprs)]
        except StopIteration:
            break

        expression = expression_stack.pop()
        stack, registry, callback = apply_token(stack, registry, expression)

        if callback:
            callback = callback.copy()
            callback.reverse()
            expression_stack.extend(callback)

    return stack

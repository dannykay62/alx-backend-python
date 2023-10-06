#!/usr/bin/env python3
"""Augmenting the code with the correct duck-typed annotations:"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a Sequence"""
    if lst:
        return lst[0]
    else:
        return None

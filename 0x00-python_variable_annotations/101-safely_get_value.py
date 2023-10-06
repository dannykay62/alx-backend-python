#!/usr/bin/env python3
"""adding type annotations to the function"""
from typing import Any, Mapping, TypeVar, Union


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[TypeVar('T'),
                       None] = None) -> Union[Any, TypeVar('T')]:
    """get a value from N Annotation safely"""
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""takes a float multiplier as argument and returns a function that
    multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function"""

    def multiplier_function(num: float) -> float:
        """Multiplies a nuber with cached number"""
        return num * multiplier

    return multiplier_function

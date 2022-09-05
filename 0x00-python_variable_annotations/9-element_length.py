
#!/usr/bin/env python3
"""
9-element_length module"""


from typing import Tuple, Sequence, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]

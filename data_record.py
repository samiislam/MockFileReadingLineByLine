"""
The DataRecord data model to store
lines of data read from a file
"""

from typing import Tuple


class DataRecord:
    """
    The DataRecord object to store
    lines of data read from a file

    Parameters
    ----------
    is_header : bool
        A flag to specify whether the read line
        consists of only labels

    items: Tuple
        A tuple of data items (can either be str
        or float)
    """

    def __init__(self, is_header: bool, items: Tuple) -> None:
        self.is_header = is_header
        self.items = items

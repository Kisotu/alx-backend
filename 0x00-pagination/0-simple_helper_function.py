#!/usr/bin/env python3
"""A function that returns a tuple of size two containing
a start index and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Gets the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    endl = start + page_size
    return (start, endl)

#!/usr/bin/python3

"""
A module that provides a function for computing the start and end indexes of a range of items to return given a page number and page size.
"""

def index_range(page, page_size):
    """
    Computes the start and end indexes of a range of items to return given a page number and page size.

    Args:
    - page (int): the page number (1-indexed)
    - page_size (int): the number of items per page

    Returns:
    A tuple of size two containing the start index (0-indexed) and end index (inclusive) of the range of items to return.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return (start_index, end_index)

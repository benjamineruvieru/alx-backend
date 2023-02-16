#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    data = []
    next_index = None

    # Check that index is in a valid range
    if index is not None:
        assert index >= 0 and index < len(self.dataset())

    # Get the data for the requested index and page_size
    if index is None:
        data = self.dataset()[:page_size]
        next_index = page_size
    else:
        data = self.dataset()[index:index+page_size]
        next_index = index + page_size

    # Remove any deleted rows from the data
    deleted_rows = self.deleted_rows()
    for deleted_row in deleted_rows:
        if deleted_row < next_index:
            # The deleted row is before the next index, so we need to adjust
            # the next index and skip the deleted row in the data
            next_index -= 1
            data = data[:deleted_row-index] + data[deleted_row-index+1:]

    return {
        "index": index,
        "next_index": next_index,
        "page_size": page_size,
        "data": data,
    }

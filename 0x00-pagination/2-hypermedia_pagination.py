#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a list of rows from the dataset corresponding to the given page and page size.
        """
        assert isinstance(page, int) and page > 0, "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size should be a positive integer"
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """Return a dictionary containing the requested page along with pagination information.
        """
        assert isinstance(page, int) and page > 0, "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size should be a positive integer"
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        data = dataset[start:end]
        total_pages = int(math.ceil(len(dataset) / page_size))
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "prev_page": prev_page,
            "next_page": next_page,
            "total_pages": total_pages
        }

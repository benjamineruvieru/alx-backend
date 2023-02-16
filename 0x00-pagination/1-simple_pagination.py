#!/usr/bin/python3
"""
Module for simple pagination of a database of popular baby names.
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
        """Returns the appropriate page of the dataset (i.e. the correct list of rows)
           based on the given page and page_size values.
        """
        assert isinstance(page, int) and page > 0, "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size should be a positive integer"
        
        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start > len(dataset):
            return []
        
        return dataset[start:end]

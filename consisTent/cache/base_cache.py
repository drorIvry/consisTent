from abc import abstractmethod

from typing import Any


class BaseCache:
    @abstractmethod
    def push_to_cache(
        self,
        item: Any,
    ):
        ...

    @abstractmethod
    def calculate_cache_distances(
        self,
        embedding,
    ):
        ...

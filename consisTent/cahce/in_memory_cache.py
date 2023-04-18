import hnswlib
from typing import Any

from .base_cache import BaseCache


class VectorCache(BaseCache):
    def __init__(
        self,
        size: int = 20,
        ef_construction: int = 200,
        space: str = "l2",
        M: int = 16,
        ef: int = 50,
    ):
        self._cache = list()
        self._size = size
        self._ef_construction = ef_construction
        self._space = space
        self._m = M
        self._ef = ef

    def push_to_cache(self, item: Any):
        if len(self._cache) > self._size:
            self._cache.pop(0)

        self._cache.append(item)

    def calculate_cache_distances(
        self,
        embedding,
    ):
        index = hnswlib.Index(
            space=self._space,
            dim=len(self._cache[0][0]),
        )

        index.init_index(
            max_elements=10000,
            ef_construction=200,
            M=16,
        )

        for item in self._cache:
            ids = [i for i in range(len(item))]

            index.add_items(
                item,
                ids,
            )

        _, distances = index.knn_query(
            embedding,
            k=len(self._cache),
        )

        return distances

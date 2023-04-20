from chromadb.api.models.Collection import Collection

from .base_cache import BaseCache


class ChromaCache(BaseCache):
    def __init__(
        self,
        collection: Collection,
        size: int = 20,
    ):
        self._collection = collection
        self._size = size
        self._cache_ids = list()

    def push_to_cache(
        self,
        document: str,
    ):
        if len(self._cache_ids) > self._size:
            id_to_remove = self._cache_ids.pop(0)
            self._collection.delete(ids=[id_to_remove])

        new_id = str(hash(document))
        self._cache_ids.append(new_id)

        self._collection.add(
            ids=[new_id],
            documents=[document],
        )

    def calculate_distance(
        self,
        query_text: str,
    ):
        if len(self._cache_ids > self._size):
            self.push_to_cache(query_text)
            return 0

        result = self._collection.query(
            query_texts=[query_text],
            n_results=len(
                self._cache_ids,
            ),
        )

        distances = result["distances"]

        return sum(distances) / len(distances)

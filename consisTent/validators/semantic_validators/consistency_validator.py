import chromadb
from chromadb.api.models.Collection import Collection


from ..base_validator import Validator
from ...cache.chroma_cache import ChromaCache


class ConsistencyValidator(Validator):
    def __init__(
        self,
        consistency_threshold: int = 1,
        seed_size: int = 20,
        client=None,
        collection: Collection = None,
    ):
        if collection is None:
            if client is None:
                client = chromadb.Client()
            collection = client.create_collection(
                name="consistency_cache",
            )
        self._cache = ChromaCache(
            collection=collection,
            size=seed_size,
        )

        self._consistency_threshold = consistency_threshold

    def validate(
        self,
        model_output: str,
    ):
        distance = self._cache.calculate_distance(model_output)
        if distance <= self._consistency_threshold:
            self._cache.push_to_cache(model_output)
            return

        raise ValueError(
            f"model output is past the consistency threshold: {self._consistency_threshold} < {distance}"  # noqa E501
        )

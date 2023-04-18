from abc import abstractmethod, ABC


class Validator(ABC):
    @abstractmethod
    def validate(model_output: str):
        ...

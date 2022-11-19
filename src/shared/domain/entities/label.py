import abc
from src.shared.helpers.errors.domain_errors import EntityError

class Label(abc.ABC):
    name: str 
    coords: dict[str, float]
    confidence: float 
    parents: list[str] 
    MIN_CONFIDENCE = 90.0

    def __init__(self, name: str, coords: dict, confidence: float, parents: list[str]):

        if (type(name) != str):
          raise EntityError('name') 
        self.name = name

        if (not coords is None and type(coords) != dict):
          raise EntityError('coords')
        self.coords = coords

        if (type(confidence) != float or confidence < self.MIN_CONFIDENCE):
          raise EntityError('confidence')
        self.confidence = confidence

        if (not coords is None and type(parents) != list):
          raise EntityError('parents')
        self.parents = parents


    def __repr__(self):
        return f"Label(name={self.name}, coords={self.coords}, confidence={self.confidence}, parents={self.parents})"
import abc
from src.shared.helpers.errors.domain_errors import EntityError

class Label(abc.ABC):
    name: str 
    coords: dict[str, float] 
    confidence: float 
    parents: str 
    MIN_CONFIDENCE = 90.0

    def __init__(self, name: str, coords: dict, confidence: float, parents: str):

        if (name == None or type(name) != str):
          raise EntityError('name') 
        self.name = name

        if (type(coords) != dict):
          raise EntityError('coords')
        self.coords = coords

        if (confidence == None or type(confidence) != float or confidence < self.MIN_CONFIDENCE):
          raise EntityError('confidence')
        self.confidence = confidence

        if (type(parents) != str):
          raise EntityError('parents')
        self.parents = parents
from abc import ABC, abstractmethod
from typing import List, Tuple


class ISubjectRepository(ABC): #todo implementar os metodos

    @abstractmethod
    async def get_all_subjects(self):
        pass

    
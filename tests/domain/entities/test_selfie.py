from src.helpers.errors.domain_errors import EntityError
from src.domain.enums.situation_enum import SITUATION
from src.domain.entities.selfie import Selfie
import datetime
import pytest

class Test_Selfie():
    def test_selfie(self):
        selfie = Selfie(
            ra= "21014442",
            dtUpload= datetime.date.today,
            url= "www.maua.br",
            situation= SITUATION.APPROVED,

        )
        
        assert type(selfie) == Selfie

    def test_selfie_error(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                ra= "21.014442",
                dtUpload= '',
                url= "",
                situation= '',
            )
      
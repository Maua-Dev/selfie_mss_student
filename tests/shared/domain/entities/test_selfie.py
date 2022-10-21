from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.selfie import Selfie
import datetime
import pytest

class Test_Selfie():
    def test_selfie(self):
        
        student = Student(
                ra="17090212",
                name="Monkey Guy",
                email="uuaa@floresta.com"
                
            )        
        
        dateCreated = datetime.datetime.now()
        
        selfie = Selfie (
                        student = student,
                        dateCreated= dateCreated,
                        url= "https://www.maua.br",
                        state= STATE.DECLINED,
                        idSelfie= 1,
                        rejectionReason = REJECTION_REASON.COVERED_FACE,
                        rejectionDescription = "Balaclava"
                        )
        
        assert type(selfie) == Selfie
        assert selfie.student == student
        assert selfie.dateCreated == dateCreated
        assert selfie.state == STATE.DECLINED
        assert selfie.rejectionReason == REJECTION_REASON.COVERED_FACE
        assert selfie.rejectionDescription == "Balaclava"

    def test_selfie_error(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17.090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )

        
    def test_selfie_error_ra_int(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra=17090212,
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )
      
    def test_selfie_error_url_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateCreated= datetime.datetime.now(),
                url= None,
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )
        
    def test_selfie_error_state_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= "PENDING_REVIEW",
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )
      
    def test_selfie_error_id_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= None,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )
        
    def test_selfie_error_id_invalid_str(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= "1",
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )

    def test_selfie_error_rejectionReason_str(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = "REJECTION_REASON.COVERED_FACE",
                rejectionDescription = "Balaclava"
            )

    def test_selfie_error_rejectionDescription_int(self):
        with pytest.raises(EntityError):
          selfie = Selfie(
                  student= Student(
                                  ra="17090212",
                                  name="Monkey Guy",
                                  email="uuaa@floresta.com"
                                  ),
                  dateCreated= datetime.datetime.now(),
                  url= "www.maua.br",
                  state= STATE.PENDING_REVIEW,
                  idSelfie= 1,
                  rejectionReason = REJECTION_REASON.COVERED_FACE,
                  rejectionDescription = 1
              )
        
    def test_selfie_error_id_invalid_negative(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= -1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava"
            )
        
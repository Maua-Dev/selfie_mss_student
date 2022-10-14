import datetime
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.update_selfie.update_selfie_usecase import UpdateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.selfie import Selfie
import pytest

class Test_UpdateSelfieUsecase:
    def test_update_selfie_usecase_name(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        usecase(ra="21010757", idSelfie=0, new_state=STATE.DECLINED, new_rejectionReason=REJECTION_REASON.NO_PERSON_RECOGNIZED, new_rejectionDescription="Please appear more")
        
        expected = Selfie(student=repo.students[0], idSelfie=0, state=STATE.DECLINED, rejectionReason=REJECTION_REASON.NO_PERSON_RECOGNIZED, rejectionDescription="Please appear more", dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),url="https://i.imgur.com/0KFBHTB.jpg",)

        assert repo.selfies[0].student.ra == expected.student.ra 
        assert repo.selfies[0].rejectionDescription == expected.rejectionDescription 
        assert repo.selfies[0].rejectionReason == expected.rejectionReason
        assert repo.selfies[0].state == expected.state 

    def test_update_selfie_usecase_state(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        usecase(ra="21010757", idSelfie=0, new_state=STATE.APPROVED)

        assert repo.selfies[0].state == STATE.APPROVED
        assert repo.selfies[0].rejectionDescription == "Balaclava"    
            
    def test_update_selfie_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                ra="21014441", idSelfie=0
            )

    def test_update_student_usecase_invalid_id(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                ra="21010757",
                idSelfie="1"
            )

 
            
import datetime
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.update_selfie.app.update_selfie_usecase import UpdateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.domain.entities.selfie import Selfie
import pytest

class Test_UpdateSelfieUsecase:
    def test_update_selfie_usecase_state_declined(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        usecase(ra="21014440", idSelfie=0, new_state=STATE.DECLINED, new_rejectionReasons=[REJECTION_REASON.NO_PERSON_RECOGNIZED], new_rejectionDescription="Please appear more")
        
        assert repo.selfies[4].student.ra == repo.students[3].ra 
        assert repo.selfies[4].rejectionDescription == "Please appear more"
        assert repo.selfies[4].rejectionReasons == [REJECTION_REASON.NO_PERSON_RECOGNIZED]
        assert repo.selfies[4].state == STATE.DECLINED

    def test_update_selfie_usecase_state_approved(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        usecase(ra="21014440", idSelfie=0, new_state=STATE.APPROVED)

        assert repo.selfies[4].state == STATE.APPROVED
            
    def test_update_selfie_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(
                ra="21015440", idSelfie=0
            )

    def test_update_student_usecase_invalid_id(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(
                ra="21010757",
                idSelfie="1"
            )

    def test_update_student_usecase_forbidden_action_approved(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(
                ra="21010757",
                idSelfie=1
            )
    def test_update_student_usecase_forbidden_action_rejected(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(
                ra="21002088",
                idSelfie=0
            )
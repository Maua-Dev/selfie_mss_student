from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.create_selfie.create_selfie_usecase import CreateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
import pytest


class Test_CreateSelfieUsecase:
    def test_create_selfie_usecase(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        lenBefore = len(repo.selfies)

        selfie = usecase(ra="21010757", url="https://www.youtube.com/watch?v=k85mRPqvMbE")

        lenAfter = lenBefore + 1

        assert len(repo.selfies) == lenAfter
        assert repo.selfies[lenAfter - 1].url == "https://www.youtube.com/watch?v=k85mRPqvMbE"
        assert repo.selfies[lenAfter - 1].student.ra == "21010757"
        assert repo.selfies[lenAfter - 1].student.name == repo.students[0].name
        assert repo.selfies[lenAfter - 1].student.email == repo.students[0].email
        assert selfie.idSelfie == 2


    def test_create_student_usecase_ra_not_found(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(ra="12345678", url="https://www.youtube.com/watch?v=k85mRPqvMbE")
            
    def test_create_student_usecase_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(ra="123456782", url="https://www.youtube.com/watch?v=k85mRPqvMbE")
            

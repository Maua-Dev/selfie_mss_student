from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.create_selfie.app.create_selfie_usecase import CreateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
import pytest


class Test_CreateSelfieUsecase:
    def test_create_selfie_usecase(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        lenBefore = len(repo.selfies)

        selfie = usecase(ra="21014442", url="https://www.youtube.com/watch?v=k85mRPqvMbE")

        lenAfter = lenBefore + 1

        assert len(repo.selfies) == lenAfter
        assert repo.selfies[lenAfter - 1].url == "https://www.youtube.com/watch?v=k85mRPqvMbE"
        assert repo.selfies[lenAfter - 1].student.ra == "21014442"
        assert repo.selfies[lenAfter - 1].student.name == repo.students[1].name
        assert repo.selfies[lenAfter - 1].student.email == repo.students[1].email
        assert selfie.idSelfie == 1


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
            
    def test_create_student_usecase_invalid_url(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(ra="21014442", url="www.mamaco.com")
            
    def test_create_student_usecase_student_have_approved_selfie(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(ra="15013103", url="www.mamaco.com")

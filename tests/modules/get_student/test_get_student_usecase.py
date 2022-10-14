from src.modules.get_student.get_student_usecase import GetStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest
class Test_GetStudentUsecase:
    def test_get_student_usecase(self):
       repo = StudentRepositoryMock()
       usecase = GetStudentUsecase(repo=repo)
       
       student = usecase(
          ra="21014442",
       )
       
       assert student == repo.students[1]
       
    def test_get_student_usecase_not_found_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
       

        with pytest.raises(NoItemsFound):
          usecase(
            ra="21014441",
          )
        
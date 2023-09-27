from src.modules.get_student.app.get_student_view_model import GetStudentViewModel
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetStudentViewModel:
    def test_get_student_view_model(self):
        repo = StudentRepositoryMock()
        student = repo.students[0]
        result = {
            "ra":"21010757",
            "name":'João Vitor Choueri Branco',
            "email":"21.01075-7@gmail.com",
            "status": "APPROVED"
        }
        
        studentViewModel = GetStudentViewModel(student, STUDENT_STATE.APPROVED).to_dict()
        
        assert studentViewModel == result
        
        
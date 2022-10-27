from src.modules.get_all_students.app.get_all_students_usecase import GetAllStudentsUsecase
from src.shared.helpers.http.http_models import OK, HttpRequest, HttpResponse
from src.modules.get_all_students.app.get_all_students_viewmodel import GetAllStudentsViewModel


class GetAllStudentsController:
    def __init__(self, usecase: GetAllStudentsUsecase):
        self.getAllStudentsUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:           
        all_students = self.getAllStudentsUsecase()
        viewmodel = GetAllStudentsViewModel(all_students)
        return OK(viewmodel.to_dict())
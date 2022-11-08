from src.modules.get_all_selfies.app.get_all_selfies_controller import GetAllSelfiesController
from src.modules.get_all_selfies.app.get_all_selfies_usecase import GetAllSelfiesUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest



class Test_GetAllSelfiesController:
    def test_get_all_selfies_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetAllSelfiesUsecase(repo=repo)
        controller = GetAllSelfiesController(usecase=usecase)

        request = HttpRequest()

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['all_selfies'][0]['url'] == repo.selfies[0].url
        assert len(response.body['all_selfies']) ==  len(repo.selfies)
        assert response.body['all_selfies'][0]['student']['ra'] == repo.selfies[0].student.ra
        assert response.body['message'] == 'all selfies were retriven'
       
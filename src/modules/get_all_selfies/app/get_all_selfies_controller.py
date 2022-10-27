from src.modules.get_all_selfies.app.get_all_selfies_usecase import GetAllSelfiesUsecase
from src.shared.helpers.http.http_models import OK, HttpRequest, HttpResponse
from src.modules.get_all_selfies.app.get_all_selfies_viewmodel import GetAllSelfiesViewModel


class GetAllSelfiesController:
    def __init__(self, usecase: GetAllSelfiesUsecase):
        self.getAllSelfiesUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:           
        all_selfies = self.getAllSelfiesUsecase()
        viewmodel = GetAllSelfiesViewModel(all_selfies)
        return OK(viewmodel.to_dict())
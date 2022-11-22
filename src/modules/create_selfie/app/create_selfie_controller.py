from src.shared.environments import Environments
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError, NotFound, Conflict, Forbidden
from .create_selfie_usecase import CreateSelfieUsecase
from .create_selfie_viewmodel import CreateSelfieViewModel


class CreateSelfieController:
    def __init__(self, usecase: CreateSelfieUsecase):
        self.createSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('ra') is None:
                raise MissingParameters('ra')

            if request.body.get('url') is None:
                raise MissingParameters('url')

            if request.body.get('automaticReview') is None:
                raise MissingParameters('automaticReview')

            # https://selfiemssstudent-stack-selfierepositorystackselfi-lezfi9mqiw4j.s3.us-east-2.amazonaws.com/19003322/selfie-2022-11-20-22%3A21%3A57-44d7d.jpeg
            url_cloudfront = f'{Environments.get_envs().cloud_front_distribution_domain}/{request.body["url"].split(".com/")[1]}'


            selfie = self.createSelfieUsecase(ra=request.body.get('ra'), url=url_cloudfront, automaticReview=request.body.get("automaticReview"))
            viewmodel = CreateSelfieViewModel(selfie)

            return Created(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except DuplicatedItem as err:
            return Conflict(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])

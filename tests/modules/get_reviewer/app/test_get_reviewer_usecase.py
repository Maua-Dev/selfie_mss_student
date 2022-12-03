

import pytest
from src.modules.get_reviewer.app.get_reviewer_usecase import GetReviewerUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_get_reviewer_usecase:
    def test_get_reviewer(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)
         
        reviewer = usecase(
            ra="03026",
         )
         
        assert reviewer == repo.reviewers[0]

    def test_get_reviewer_ra_not_found(self):
        repo = StudentRepositoryMock()
        usecase = GetReviewerUsecase(repo=repo)


        with pytest.raises(NoItemsFound):
          usecase(
            ra="77777",
          )
        
from src.modules.get_reviewer.app.get_reviewer_viewmodel import GetReviewerViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetReviewerViewModel:
    def test_get_student_view_model(self):

        repo = StudentRepositoryMock()
        reviewer = repo.reviewers[0]
        result =   {'active': True,
                    'email': 'mauro@maua.br',
                    'message': 'reviewer was retrieved',
                    'name': 'Mauro Crapino',
                    'ra': '03026'
                  }
        
        reviewerViewModel = GetReviewerViewModel(reviewer).to_dict()
        
        assert reviewerViewModel == result
        
        
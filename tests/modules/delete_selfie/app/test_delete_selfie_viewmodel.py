from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.delete_selfie.app.delete_selfie_viewmodel import DeleteSelfieViewModel

class Test_DeleteSelfieViewModel:
    def test_get_selfie_view_model(self):
        repo = StudentRepositoryMock()
        selfie = repo.selfies[0]
        student = repo.students[0]
        result = {
                  'message': 'the selfie was deleted',
                  'selfie': {'automaticReview': {'automaticallyRejected': True,
                                                 'labels': [{'confidence': 98.54370880126953,
                                                             'coords': {'Height': 0.8659809827804565,
                                                                        'Left': 0.012313545681536198,
                                                                        'Top': 0.11108686774969101,
                                                                        'Width': 0.9711952805519104},
                                                             'name': 'Person',
                                                             'parents': []},
                                                            {'confidence': 98.54370880126953,
                                                             'coords': {'Height': 0.8659809827804565,
                                                                        'Left': 0.012313545681536198,
                                                                        'Top': 0.11108686774969101,
                                                                        'Width': 0.9711952805519104},
                                                             'name': 'Hat',
                                                             'parents': []},
                                                            {'confidence': 98.54370880126953,
                                                             'coords': {'Height': 0.8659809827804565,
                                                                        'Left': 0.012313545681536198,
                                                                        'Top': 0.11108686774969101,
                                                                        'Width': 0.9711952805519104},
                                                             'name': 'Face',
                                                             'parents': []}],
                                                 'rejectionReason': 'COVERED_FACE'},
                             'dateCreated': '2022-10-01T16:01:59.149927',
                             'idSelfie': 0,
                             'rejectionDescription': 'Balaclava',
                             'rejectionReason': 'COVERED_FACE',
                             'state': 'DECLINED',
                             'url': 'https://i.imgur.com/0KFBHTB.jpg'},
                  'student': {'email': 'eusousoller@gmail.com',
                              'name': 'Victor',
                              'ra': '21010757'},
                    }
     
        
        studentViewModel = DeleteSelfieViewModel(data=selfie, student=student).to_dict()
        
        assert studentViewModel == result
        
        
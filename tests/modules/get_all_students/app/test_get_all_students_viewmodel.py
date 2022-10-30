from src.modules.get_all_students.app.get_all_students_viewmodel import GetAllStudentsViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_all_students.app.get_all_students_usecase import GetAllStudentsUsecase
class Test_GetAllStudentsViewModel:
    def test_get_all_student_view_model(self):
        repo = StudentRepositoryMock()
        usecase = GetAllStudentsUsecase(repo=repo)
        all_students = usecase()

        expected = {
         
           'all_students': {'15013103': {'email': 'iamronald@mageofprogramming.com.br',
                                         'name': 'Little Ronald',
                                         'selfies': [{'dateCreated': '2022-10-01T16:01:59.149927',
                                                      'idSelfie': 0,
                                                      'rejectionDescription': 'Usou '
                                                                              'chapéu de '
                                                                              'mexicano '
                                                                              'que '
                                                                              'cobriu a '
                                                                              'cara',
                                                      'rejectionReason': 'COVERED_FACE',
                                                      'state': 'DECLINED',
                                                      'url': 'https://i.imgur.com/4ewA19S.png'},
                                                     {'dateCreated': '2022-10-02T16:01:59.149927',
                                                      'idSelfie': 1,
                                                      'rejectionDescription': 'Tirou '
                                                                              'foto no '
                                                                              'meio da '
                                                                              'Rave, '
                                                                              'enquanto '
                                                                              'aparecia '
                                                                              'um brilho '
                                                                              'forte',
                                                      'rejectionReason': 'NOT_ALLOWED_BACKGROUND',
                                                      'state': 'DECLINED',
                                                      'url': 'https://i.imgur.com/4ewA19S.png'},
                                                     {'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 2,
                                                      'rejectionDescription': '',
                                                      'rejectionReason': 'NONE',
                                                      'state': 'APPROVED',
                                                      'url': 'https://i.imgur.com/4ewA19S.png'},
                                                     {'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 2,
                                                      'rejectionDescription': '',
                                                      'rejectionReason': 'NONE',
                                                      'state': 'APPROVED',
                                                      'url': 'https://i.imgur.com/4ewA19S.png'}],
                                         'status': 'APPROVED'},
                            '17090212': {'email': 'uuaa@floresta.com',
                                         'name': 'Monkey Guy',
                                         'selfies': [],
                                         'status': 'NO_SELFIE'},
                            '21002088': {'email': 'mvergani.enactusmaua@gmail.com',
                                         'name': 'Maluzinha',
                                         'selfies': [{'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 0,
                                                      'rejectionDescription': 'O brilho '
                                                                              'dos olhos '
                                                                              'dela é '
                                                                              'senscaional',
                                                      'rejectionReason': 'NOT_ALLOWED_BACKGROUND',
                                                      'state': 'DECLINED',
                                                      'url': 'https://i.imgur.com/4ewA19S.png'}],
                                         'status': 'SELFIE_REJECTED'},
                            '21010757': {'email': 'eusousoller@gmail.com',
                                         'name': 'Victor',
                                         'selfies': [{'dateCreated': '2022-10-01T16:01:59.149927',
                                                      'idSelfie': 0,
                                                      'rejectionDescription': 'Balaclava',
                                                      'rejectionReason': 'COVERED_FACE',
                                                      'state': 'DECLINED',
                                                      'url': 'https://i.imgur.com/0KFBHTB.jpg'},
                                                     {'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 1,
                                                      'rejectionDescription': '',
                                                      'rejectionReason': 'NONE',
                                                      'state': 'APPROVED',
                                                      'url': 'https://i.imgur.com/b9qFYmb.jpg'}],
                                         'status': 'APPROVED'},
                            '21014440': {'email': 'eusouoawsboy@amazon.com',
                                         'name': 'Eh o Vilas do Mockas',
                                         'selfies': [{'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 0,
                                                      'rejectionDescription': '',
                                                      'rejectionReason': 'NONE',
                                                      'state': 'IN_REVIEW',
                                                      'url': 'https://i.imgur.com/4ewA19S.png'}],
                                         'status': 'SELFIE_IN_REVIEW'},
                            '21014442': {'email': 'eutambemsousoler@outlook.com',
                                         'name': 'Soller',
                                         'selfies': [{'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 0,
                                                      'rejectionDescription': '',
                                                      'rejectionReason': 'NONE',
                                                      'state': 'PENDING_REVIEW',
                                                      'url': 'https://i.imgur.com/dv7Q5VT.jpg'}],
                                         'status': 'SELFIE_PENDING_REVIEW'},
                            '21014443': {'email': 'acreditaquesousollertambem@yahoo.com',
                                         'name': 'Guirão',
                                         'selfies': [{'dateCreated': '2022-10-12T16:01:59.149927',
                                                      'idSelfie': 0,
                                                      'rejectionDescription': '',
                                                      'rejectionReason': 'NONE',
                                                      'state': 'APPROVED',
                                                      'url': 'https://pps.whatsapp.net/v/t61.24694-24/56153869_1240493612792530_7354067850044112896_n.jpg?ccb=11-4&oh=01_AVydS_LW2WM2tLLKeEKbZIAlVJCbgJlfZ96y3yQnXAFBEA&oe=635822E5'}],
                                         'status': 'APPROVED'}},
           'message': 'the students were retriven',
          }
         
        
        allStudentsViewModel = GetAllStudentsViewModel(all_students).to_dict()
        
        assert allStudentsViewModel == expected
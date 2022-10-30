from src.modules.get_all_selfies.app.get_all_selfies_viewmodel import GetAllSelfiesViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetAllSelfiesViewModel:
    def test_get_all_selfie_view_model(self):
        repo = StudentRepositoryMock()
        all_selfies = repo.selfies

        result = {
       'all_selfies': [{'dateCreated': '2022-10-01T16:01:59.149927',
                         'idSelfie': 0,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': 'Balaclava',
                         'rejectionReason': 'COVERED_FACE',
                         'state': 'DECLINED',
                         'student': {'email': 'eusousoller@gmail.com',
                                     'name': 'Victor',
                                     'ra': '21010757'},
                         'url': 'https://i.imgur.com/0KFBHTB.jpg'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 1,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': '',
                         'rejectionReason': 'NONE',
                         'state': 'APPROVED',
                         'student': {'email': 'eusousoller@gmail.com',
                                     'name': 'Victor',
                                     'ra': '21010757'},
                         'url': 'https://i.imgur.com/b9qFYmb.jpg'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 0,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': '',
                         'rejectionReason': 'NONE',
                         'state': 'PENDING_REVIEW',
                         'student': {'email': 'eutambemsousoler@outlook.com',
                                     'name': 'Soller',
                                     'ra': '21014442'},
                         'url': 'https://i.imgur.com/dv7Q5VT.jpg'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 0,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': '',
                         'rejectionReason': 'NONE',
                         'state': 'APPROVED',
                         'student': {'email': 'acreditaquesousollertambem@yahoo.com',        
                                     'name': 'Guirão',
                                     'ra': '21014443'},
                         'url': 'https://pps.whatsapp.net/v/t61.24694-24/56153869_1240493612792530_7354067850044112896_n.jpg?ccb=11-4&oh=01_AVydS_LW2WM2tLLKeEKbZIAlVJCbgJlfZ96y3yQnXAFBEA&oe=635822E5'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 0,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': '',
                         'rejectionReason': 'NONE',
                         'state': 'IN_REVIEW',
                         'student': {'email': 'eusouoawsboy@amazon.com',
                                     'name': 'Eh o Vilas do Mockas',
                                     'ra': '21014440'},
                         'url': 'https://i.imgur.com/4ewA19S.png'},
                        {'dateCreated': '2022-10-01T16:01:59.149927',
                         'idSelfie': 0,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': 'Usou chapéu de mexicano que cobriu '       
                                                 'a cara',
                         'rejectionReason': 'COVERED_FACE',
                         'state': 'DECLINED',
                         'student': {'email': 'iamronald@mageofprogramming.com.br',
                                     'name': 'Little Ronald',
                                     'ra': '15013103'},
                         'url': 'https://i.imgur.com/4ewA19S.png'},
                        {'dateCreated': '2022-10-02T16:01:59.149927',
                         'idSelfie': 1,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': 'Tirou foto no meio da Rave, '
                                                 'enquanto aparecia um brilho forte',        
                         'rejectionReason': 'NOT_ALLOWED_BACKGROUND',
                         'state': 'DECLINED',
                         'student': {'email': 'iamronald@mageofprogramming.com.br',
                                     'name': 'Little Ronald',
                                     'ra': '15013103'},
                         'url': 'https://i.imgur.com/4ewA19S.png'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 2,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': '',
                         'rejectionReason': 'NONE',
                         'state': 'APPROVED',
                         'student': {'email': 'iamronald@mageofprogramming.com.br',
                                     'name': 'Little Ronald',
                                     'ra': '15013103'},
                         'url': 'https://i.imgur.com/4ewA19S.png'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 2,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': '',
                         'rejectionReason': 'NONE',
                         'state': 'APPROVED',
                         'student': {'email': 'iamronald@mageofprogramming.com.br',
                                     'name': 'Little Ronald',
                                     'ra': '15013103'},
                         'url': 'https://i.imgur.com/4ewA19S.png'},
                        {'dateCreated': '2022-10-12T16:01:59.149927',
                         'idSelfie': 0,
                         'message': 'the selfie was retriven',
                         'rejectionDescription': 'O brilho dos olhos dela é senscaional',
                         'rejectionReason': 'NOT_ALLOWED_BACKGROUND',
                         'state': 'DECLINED',
                         'student': {'email': 'mvergani.enactusmaua@gmail.com',
                                     'name': 'Maluzinha',
                                     'ra': '21002088'},
                         'url': 'https://i.imgur.com/4ewA19S.png'}],
            "message": "all selfies were retriven"
        }
        
        allSelfiesViewModel = GetAllSelfiesViewModel(all_selfies).to_dict()
        
        assert allSelfiesViewModel == result
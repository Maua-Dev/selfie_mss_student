from src.modules.get_all_students.app.get_all_students_controller import GetAllStudentsController
from src.modules.get_all_students.app.get_all_students_usecase import GetAllStudentsUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest



class Test_GetAllStudentsController:
    def test_get_all_students_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetAllStudentsUsecase(repo=repo)
        controller = GetAllStudentsController(usecase=usecase)

        request = HttpRequest()

        response = controller(request=request)

        expected = {'all_students': {'21010757': {'name': 'João Vitor Choueri Branco', 'email': '21.01075-7@gmail.com', 'status': 'APPROVED', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-01T16:01:59.149927', 'url': 'https://i.imgur.com/0KFBHTB.jpg', 'state': 'DECLINED', 'rejectionReasons': ['COVERED_FACE'], 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['COVERED_FACE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Hat', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': 'Balaclava'}, {'idSelfie': 1, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/b9qFYmb.jpg', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': ''}]}, '21014442': {'name': 'Vitor Guirão Soller', 'email': 'eutambemsousoler@outlook.com', 'status': 'SELFIE_PENDING_REVIEW', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/dv7Q5VT.jpg', 'state': 'PENDING_REVIEW', 'rejectionReasons': ['NONE'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': ''}]}, '21014443': {'name': 'Guirão', 'email': 'acreditaquesousollertambem@yahoo.com', 'status': 'APPROVED', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/6a7qqRg.jpg', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': ''}]}, '21014440': {'name': 'Eh o Vilas do Mockas', 'email': 'eusouoawsboy@amazon.com', 'status': 'SELFIE_IN_REVIEW', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'IN_REVIEW', 'rejectionReasons': ['NONE'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 99.12312312, 'parents': []}]}, 'rejectionDescription': ''}]}, '17090212': {'name': 'Monkey Guy', 'email': 'uuaa@floresta.com', 'status': 'NO_SELFIE', 'selfies': []}, '15013103': {'name': 'Little Ronald', 'email': 'iamronald@mageofprogramming.com.br', 'status': 'APPROVED', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-01T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['COVERED_FACE'], 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['COVERED_FACE'], 'labels': [{'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Hat', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Human', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': 'Usou chapéu de mexicano que cobriu a cara'}, {'idSelfie': 1, 'dateCreated': '2022-10-02T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'labels': [{'name': 'Building', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.13214, 'parents': ['Architecture']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': 'Tirou foto no meio da Rave, enquanto aparecia um brilho forte'}, {'idSelfie': 2, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NONE'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'rejectionDescription': ''}, {'idSelfie': 3, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}, 'rejectionDescription': ''}]}, '21002088': {'name': 'Maluzinha', 'email': 'mvergani.enactusmaua@gmail.com', 'status': 'SELFIE_REJECTED', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}, 'rejectionDescription': 'O brilho dos olhos dela é senscaional'}]}, '21012345': {'name': 'Hater de Regra de Negocio', 'email': 'buisinnes.rules@must.die.com', 'status': 'SELFIE_IN_REVIEW', 'selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/41wA18S.png', 'state': 'IN_REVIEW', 'rejectionReasons': [], 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}, 'rejectionDescription': ''}]}}, 'message': 'the students were retriven'}
        
        assert response.status_code == 200
        assert len(response.body['all_students']) ==  len(repo.students)
        assert response.body == expected
        

       
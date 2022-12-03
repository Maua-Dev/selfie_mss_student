from src.modules.get_all_selfies.app.get_all_selfies_viewmodel import GetAllSelfiesViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetAllSelfiesViewModel:
    def test_get_all_selfie_view_model(self):
        repo = StudentRepositoryMock()
        all_selfies = repo.selfies

        result = {'all_selfies': [{'idSelfie': 0, 'dateCreated': '2022-10-01T16:01:59.149927', 'url': 'https://i.imgur.com/0KFBHTB.jpg', 'state': 'DECLINED', 'rejectionReasons': ['COVERED_FACE'], 'rejectionDescription': 'Balaclava', 'student': {'ra': '21010757', 'email': 'eusousoller@gmail.com', 'name': 'Victor'}, 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['COVERED_FACE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Hat', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 1, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/b9qFYmb.jpg', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'student': {'ra': '21010757', 'email': 'eusousoller@gmail.com', 'name': 'Victor'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/dv7Q5VT.jpg', 'state': 'PENDING_REVIEW', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'student': {'ra': '21014442', 'email': 'eutambemsousoler@outlook.com', 'name': 'Soller'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/6a7qqRg.jpg', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'student': {'ra': '21014443', 'email': 'acreditaquesousollertambem@yahoo.com', 'name': 'Guirão'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'IN_REVIEW', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'student': {'ra': '21014440', 'email': 'eusouoawsboy@amazon.com', 'name': 'Eh o Vilas do Mockas'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 99.12312312, 'parents': []}]}}, {'idSelfie': 0, 'dateCreated': '2022-10-01T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['COVERED_FACE'], 'rejectionDescription': 'Usou chapéu de mexicano que cobriu a cara', 'student': {'ra': '15013103', 'email': 'iamronald@mageofprogramming.com.br', 'name': 'Little Ronald'}, 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['COVERED_FACE'], 'labels': [{'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Hat', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Human', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 1, 'dateCreated': '2022-10-02T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'rejectionDescription': 'Tirou foto no meio da Rave, enquanto aparecia um brilho forte', 'student': {'ra': '15013103', 'email': 'iamronald@mageofprogramming.com.br', 'name': 'Little Ronald'}, 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'labels': [{'name': 'Building', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.13214, 'parents': ['Architecture']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 2, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'student': {'ra': '15013103', 'email': 'iamronald@mageofprogramming.com.br', 'name': 'Little Ronald'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, {'idSelfie': 3, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'student': {'ra': '15013103', 'email': 'iamronald@mageofprogramming.com.br', 'name': 'Little Ronald'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}}, {'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'rejectionDescription': 'O brilho dos olhos dela é senscaional', 'student': {'ra': '21002088', 'email': 'mvergani.enactusmaua@gmail.com', 'name': 'Maluzinha'}, 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}}], 'message': 'all selfies were retriven'}

        allSelfiesViewModel = GetAllSelfiesViewModel(all_selfies).to_dict()
        
        assert allSelfiesViewModel == result
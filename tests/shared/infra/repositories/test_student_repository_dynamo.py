from src.shared.infra.repositories.student_repository_dynamo import StudentRepositoryDynamo
import os


class Test_StudentRepositoryDynamo:

    def test_get_selfie(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        resp = student_repository.get_selfie("19003315", 0)
        assert True

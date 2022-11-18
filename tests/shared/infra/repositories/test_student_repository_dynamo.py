import pytest

from src.shared.infra.repositories.student_repository_dynamo import StudentRepositoryDynamo
import os

from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_StudentRepositoryDynamo:

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_selfie(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        resp = student_repository.get_selfie("21010757", 0)
        assert True

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_student(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        resp = student_repository.get_student("19003315")
        assert True

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_student(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.create_student(student_repository_mock.students[0])

        assert True

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_selfie(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.create_selfie(student_repository_mock.selfies[0])

        assert True



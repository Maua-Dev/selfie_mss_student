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

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_student(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.update_student(student_repository_mock.students[0].ra, new_name="Teste", new_email="testinha@test.com")

        old_student = student_repository_mock.students[0]
        old_student.name = "Teste"
        old_student.email = "testinha@test.com"

        assert resp.name == old_student.name
        assert resp.email == old_student.email
        assert resp.ra == old_student.ra

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_student(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.delete_student(student_repository_mock.students[0].ra)

        assert resp.name == student_repository_mock.students[0].name
        assert resp.email == student_repository_mock.students[0].email
        assert resp.ra == student_repository_mock.students[0].ra

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_selfies_by_ra(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.get_selfies_by_ra(student_repository_mock.students[0].ra)

        assert True

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_selfie(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.delete_selfie(student_repository_mock.selfies[0].student.ra, student_repository_mock.selfies[0].idSelfie)


        assert True

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_selfies(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.get_all_selfies()

        assert len(resp) == len(student_repository_mock.selfies)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_students(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.get_all_students()

        assert len(resp) == len(student_repository_mock.students)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_students_by_name(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.get_all_students_by_name("Teste")

        assert len(resp) == len(student_repository_mock.students)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_students_by_ra(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.get_all_students_by_ra("19003315")

        assert len(resp) == len(student_repository_mock.students)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_students(self):
        os.environ["STAGE"] = "TEST"

        student_repository = StudentRepositoryDynamo()
        student_repository_mock = StudentRepositoryMock()
        resp = student_repository.get_all_students()

        assert len(resp) == len(student_repository_mock.students)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_reviewer(self):
        os.environ["STAGE"] = "TEST"

        repo_dynamo = StudentRepositoryDynamo()
        repo_mock = StudentRepositoryMock()
        resp = repo_dynamo.create_reviewer(reviewer=repo_mock.reviewers[0])

        assert resp.__repr__ == repo_mock.reviewers[0].__repr__

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_reviewer(self):
        os.environ["STAGE"] = "TEST"

        repo_dynamo = StudentRepositoryDynamo()
        resp = repo_dynamo.update_reviewer(ra="03026", new_active=False)

        assert resp.active == False
        assert resp.name == "Mauro Crapino"

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_reviewer(self):
        os.environ["STAGE"] = "TEST"

        repo_dynamo = StudentRepositoryDynamo()
        repo_mock = StudentRepositoryMock()
        resp = repo_dynamo.delete_reviewer(ra="03026")


        assert resp.__dict__ == repo_mock.reviewers[0].__dict__

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_reviewer(self):
        os.environ["STAGE"] = "TEST"

        repo_dynamo = StudentRepositoryDynamo()
        repo_mock = StudentRepositoryMock()
        resp = repo_dynamo.get_reviewer(ra="03026")


        assert resp.__dict__ == repo_mock.reviewers[0].__dict__

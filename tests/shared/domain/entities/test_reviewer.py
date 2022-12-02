import pytest
from src.shared.domain.entities.reviwer import Reviewer
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError


class Test_Reviewer():
    def test_reviewer(self):
        reviewer = Reviewer(ra="03026", name="Mauro Crapino",
                          email="mauro@maua.br", active=True)

        assert type(reviewer) == Reviewer

    def test_reviewer_ra_is_none(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra=None, name="Mauro Crapino", email="mauro@maua.br", active=True)

    def test_reviewer_ra_is_not_string(self):
        with pytest.raises(EntityParameterTypeError):
            reviewer = Reviewer(ra=123, name="Mauro Crapino", email="mauro@maua.br", active=True)

    def test_reviewer_ra_is_not_valid(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="123456789", name="Mauro Crapino", email="mauro@maua.br", active=True)

    def test_reviewer_ra_is_not_valid_special_char(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="0-302.6", name="Mauro Crapino", email="mauro@maua.br", active=True)

    def test_reviewer_name_is_none(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="03026", name=None, email="mauro@maua.br", active=True)

    def test_reviewer_name_is_not_valid(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="03026", name="M", email="mauro@maua.br", active=True)

    def test_reviewer_email_is_none(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="03026", name="Mauro Crapino", email=None, active=True)

    def test_reviewer_email_is_not_valid(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="03026", name="Mauro Crapino", email="mauro@maua", active=True)
    
    def test_reviewer_active_is_not_bool(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="03026", name="Mauro Crapino", email="mauro@maua.br", active="True")

    def test_reviewer_active_is_none(self):
        with pytest.raises(EntityError):
            reviewer = Reviewer(ra="03026", name="Mauro Crapino", email="mauro@maua.br", active=None)
    
    


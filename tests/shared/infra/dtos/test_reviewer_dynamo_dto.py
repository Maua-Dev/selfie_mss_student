from src.shared.infra.dtos.reviewer_dynamo_dto import ReviewerDynamoDTO
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_ReviewerDynamoDTO:
    def test_from_entity(self):
        repo = StudentRepositoryMock()      
        reviewer_entity = repo.reviewers[0]
        
        assert ReviewerDynamoDTO.from_entity(reviewer=reviewer_entity).__dict__ == {
                                                                    "ra":reviewer_entity.ra,
                                                                    "name":reviewer_entity.name,
                                                                    "email":reviewer_entity.email,
                                                                    "active":reviewer_entity.active
                                                                }
        
    def test_to_dynamo(self):
        repo = StudentRepositoryMock()      
        reviewer_dto = ReviewerDynamoDTO.from_entity(reviewer=repo.reviewers[0])
        
        assert reviewer_dto.to_dynamo() == {
                                                "entity": "reviewer",
                                                "ra":reviewer_dto.ra,
                                                "name":reviewer_dto.name,
                                                "email":reviewer_dto.email,
                                                "active":reviewer_dto.active
                                            }
        
    
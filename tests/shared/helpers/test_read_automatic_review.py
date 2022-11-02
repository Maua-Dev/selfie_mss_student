import pytest
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.functions.read_automatic_review import read_automatic_review
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.helpers.errors.controller_errors import MissingParameters

class Test_read_automatic_review:
    def test_read_automatic_review(self):
        automatic_review_dict = {
            "automaticallyRejected": "True",
            "rejectionReason": "COVERED_FACE",
            "labels": [{
                            "name": "Glasses",
                            "coords": {
                                    "Width": "0.6591288447380066",
                                    "Height": "0.17444363236427307",
                                    "Left": "0.19148917496204376",
                                    "Top": "0.3813813030719757"
                            },
                            "confidence": "94.5357666015625",
                            "parents": ["Accessories"],
                        },
                        {
                            "name": "Blalblas",
                            "coords": {
                                    "Width": "0.6591288480066",
                                    "Height": "0.1744236427307",
                                    "Left": "0.19148916204376",
                                    "Top": "0.3813813719757"
                            },
                            "confidence": "95.5366015625",
                            "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                        }]
                  }
        
        result = read_automatic_review(automaticReview=automatic_review_dict)
        
        expected = AutomaticReview(
            automaticallyRejected = True,
            rejectionReason = REJECTION_REASON.COVERED_FACE,
            labels = [
                Label(
                    name="Glasses",
                    coords={
                                "Width": 0.6591288447380066,
                                "Height": 0.17444363236427307,
                                "Left": 0.19148917496204376,
                                "Top": 0.3813813030719757
                            },
                    confidence=94.5357666015625,
                    parents=["Accessories"],
                ),
                Label(
                    name="Blalblas",
                    coords={
                                "Width": 0.6591288480066,
                                "Height": 0.1744236427307,
                                "Left": 0.19148916204376,
                                "Top": 0.3813813719757
                            },
                    confidence=95.5366015625,
                    parents=["ASODnoasdsa", "nmdokasnkndkasnkd"],
                )
            ]
        )
        
        assert result.automaticallyRejected  == expected.automaticallyRejected
        assert result.rejectionReason  == expected.rejectionReason
        
        assert result.labels[0].name  == expected.labels[0].name
        assert result.labels[0].coords  == expected.labels[0].coords
        assert result.labels[0].confidence  == expected.labels[0].confidence
        assert result.labels[0].parents  == expected.labels[0].parents
        
        assert result.labels[1].name  == expected.labels[1].name
        assert result.labels[1].coords  == expected.labels[1].coords
        assert result.labels[1].confidence  == expected.labels[1].confidence
        assert result.labels[1].parents  == expected.labels[1].parents

    def test_read_automatic_review_missing_parameters(self):
            automatic_review_dict = {
            "automaticallyRejected": "True",
            "rejectionReason": "COVERED_FACE",
            "labels": [{
                            "name": "Glasses",
                            "coords": {
                                    "Width": "0.6591288447380066",
                                    "Height": "0.17444363236427307",
                                    "Left": "0.19148917496204376",
                                    "Top": "0.3813813030719757"
                            },
                            "confidence": "94.5357666015625",
                            "parents": ["Accessories"],
                        },
                        {
                            "name": "Blalblas",
                            "coords": {
                                    "Width": "0.6591288480066",
                                    "Left": "0.19148916204376",
                                    "Top": "0.3813813719757"
                            },
                            "confidence": "95.5366015625",
                            "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                        }]
                  }
            with pytest.raises(MissingParameters):
                automaticReview = read_automatic_review(automaticReview=automatic_review_dict)
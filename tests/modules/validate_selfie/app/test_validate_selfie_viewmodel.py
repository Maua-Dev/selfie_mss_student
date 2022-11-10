import pytest 
from src.modules.validate_selfie.app.validate_selfie_viewmodel import ValidateSelfieViewModel
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class Test_ValidadeSelfieViewModel:
    def validate_selfie_viewmodel(self):
        data = AutomaticReview(
            automaticallyRejected=True,
            rejectionReasons=[REJECTION_REASON.NOT_ALLOWED_BACKGROUND, REJECTION_REASON.NO_PERSON_RECOGNIZED],
            labels=[
                Label(
                    name="Building",
                    coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                    confidence=98.13214,
                    parents=["Architecture"]
                    ),
                Label(
                    name="Face",
                    coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                    confidence=98.54370880126953,
                    parents=[]
                )
            ]
        )     
    
        viewmodel = ValidateSelfieViewModel(data=data)
        
        assert viewmodel.to_dict() == {}

from src.shared.domain.entities.label import Label
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_AutomaticReview():
    def test_automatic_review(self):
        
        labels = [Label(
          name="Brown Hair",
          coords={},
          confidence=98.979095458984383,
          parents=[],
        ), 
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
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents=[],
        )]
        
        automatic_review = AutomaticReview(
            automaticallyRejected = True,
            rejectionReason = REJECTION_REASON.COVERED_FACE,
            labels = labels
        )
        
        assert automatic_review.automaticallyRejected == True
        assert automatic_review.rejectionReason == REJECTION_REASON.COVERED_FACE
        assert automatic_review.labels[0] == labels[0]
        
    def test_automatic_review_automaticallyRejected_empty_field(self):
    
        labels = [Label(
          name="Brown Hair",
          coords={},
          confidence=98.979095458984383,
          parents=[],
        ), 
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
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents=[],
        )]


        with pytest.raises(EntityError):
           automatic_review = AutomaticReview(
            automaticallyRejected= None,
            rejectionReason = REJECTION_REASON.COVERED_FACE,
            labels = labels
        )

    def test_automatic_review_automaticallyRejected_not_bool(self):
    
        labels = [Label(
          name="Brown Hair",
          coords={},
          confidence=98.979095458984383,
          parents=[],
        ), 
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
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents=[],
        )]


        with pytest.raises(EntityError):
           automatic_review = AutomaticReview(
            automaticallyRejected= 1,
            rejectionReason = REJECTION_REASON.COVERED_FACE,
            labels = labels
        )
    
    
    def test_automatic_review_rejectionReason_empty_field(self):
          
        labels = [Label(
          name="Brown Hair",
          coords={},
          confidence=98.979095458984383,
          parents=[],
        ), 
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
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents=[],
        )]
        
        with pytest.raises(EntityError):
          automatic_review = AutomaticReview(
              automaticallyRejected = True,
              rejectionReason = None,
              labels = labels
          )
        
      
    def test_automatic_review_rejectionReason_not_rejection_reason(self):
        labels = [Label(
          name="Brown Hair",
          coords={},
          confidence=98.979095458984383,
          parents=[],
        ), 
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
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents=[],
        )]
        
        with pytest.raises(EntityError):
          automatic_review = AutomaticReview(
              automaticallyRejected = True,
              rejectionReason = 1,
              labels = labels
          )
        
    def test_automatic_review_labels_empty_list(self):
        with pytest.raises(EntityError):
              automatic_review = AutomaticReview(
                  automaticallyRejected= True,
                  rejectionReason = REJECTION_REASON.COVERED_FACE,
                  labels = []
              )
        
      
    def test_automatic_review_labels_not_list(self):
        with pytest.raises(EntityError):
            automatic_review = AutomaticReview(
                automaticallyRejected= True,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                labels = "[]"
            )
        
    
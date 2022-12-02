

import datetime

import pytest
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviwer import Reviewer
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Review():

  SELFIE = Selfie(
                idSelfie=0,
                  student= Student(
                  ra="21010757",
                  name="Victor",
                  email="eusousoller@gmail.com"
                  ),
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.IN_REVIEW,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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
                        ),
                        Label(
                            name="Face",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=99.12312312,
                            parents=[],
                        ),
                    ]
                )
            )
      
  REVIEWER = Student(
                  ra="21010757",
                  name="Victor",
                  email="eusousoller@gmail.com"
                  )

  def test_review(self):
    review = Review(
      reviewId=1,
      state=REVIEW_STATE.PENDING_VALIDATION,
      reviewer=Reviewer(ra="03026", name="Mauro Crapino",
                          email="mauro@maua.br", active=True),
      selfie=Selfie(
                idSelfie=0,
                   student= Student(
                  ra="21010757",
                  name="Victor",
                  email="eusousoller@gmail.com"
                  ),
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.IN_REVIEW,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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
                        ),
                        Label(
                            name="Face",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=99.12312312,
                            parents=[],
                        ),
                    ]
                )
            ),
      dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
      dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
    )

    assert type(review) == Review
    assert review.reviewId == 1 
    assert review.state == REVIEW_STATE.PENDING_VALIDATION
    assert review.reviewer.ra == "03026"
    assert review.reviewer.name == "Mauro Crapino"
    assert review.reviewer.email == "mauro@maua.br"
    assert review.reviewer.active == True
    assert review.selfie.idSelfie == 0
    assert review.selfie.student.ra == "21010757"
    assert review.selfie.student.name == "Victor"
    assert review.selfie.dateCreated == datetime.datetime(2022, 10, 12, 16, 1, 59, 149927)
    assert review.selfie.url == "https://i.imgur.com/4ewA19S.png"
    assert review.selfie.state == STATE.IN_REVIEW
    assert review.selfie.rejectionReasons == [REJECTION_REASON.NONE]
    assert review.selfie.rejectionDescription == ""
    assert review.selfie.automaticReview.automaticallyRejected == False
    assert review.selfie.automaticReview.rejectionReasons == [REJECTION_REASON.NONE]
    assert review.selfie.automaticReview.labels[0].name == "Person"      
    assert review.dateAssigned == datetime.datetime(2022, 12, 1, 16, 1, 59, 149927)
    assert review.dateReviewed == datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)

  def test_review_with_no_reviewer(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=None,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_no_selfie(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=None,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )
    
  def test_review_with_no_date_assigned(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=None,
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_no_date_reviewed(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=None
      )
    
  def test_review_with_no_review_id(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=None,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_no_state(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=None,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_invalid_state(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state="INVALID_STATE",
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )
    
  def test_review_with_invalid_date_assigned(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned="INVALID_DATE",
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_invalid_date_reviewed(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed="INVALID_DATE"
      )

  def test_review_with_invalid_review_id(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId="INVALID_ID",
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_invalid_reviewer(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer="INVALID_REVIEWER",
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_invalid_selfie(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie="INVALID_SELFIE",
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_invalid_date_assigned(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned="INVALID_DATE",
        dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
      )

  def test_review_with_invalid_date_reviewed(self):
    with pytest.raises(EntityError):
      review = Review(
        reviewId=1,
        state=REVIEW_STATE.PENDING_VALIDATION,
        reviewer=self.REVIEWER,
        selfie=self.SELFIE,
        dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
        dateReviewed="INVALID_DATE"
      )
      
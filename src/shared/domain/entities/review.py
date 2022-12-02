import abc
import datetime

from src.shared.domain.entities.reviwer import Reviewer
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.helpers.errors.domain_errors import EntityError

class Review(abc.ABC):
  reviewId: int
  state: REVIEW_STATE
  reviewer: Reviewer
  selfie: Selfie
  dateAssigned: datetime.datetime
  dateReviewed: datetime.datetime
  REVIEW_MAXIMUM_PENDING_DAYS: int = 3 #days

  def __init__(self, reviewId: int, state: REVIEW_STATE, reviewer: Reviewer, selfie: Selfie, dateAssigned: datetime.datetime, dateReviewed: datetime.datetime):

    if (reviewId == None or type(reviewId) != int):
      raise EntityError('reviewId')
    self.reviewId = reviewId

    if state == None or type(state) != REVIEW_STATE:
      raise EntityError('state')
    self.state = state

    if reviewer == None or type(reviewer) != Reviewer:
      raise EntityError('reviewer')
    self.reviewer = reviewer

    if selfie == None or type(selfie) != Selfie:
      raise EntityError('selfie')
    self.selfie = selfie 
  
    if (dateAssigned == None and type(dateAssigned) != datetime.datetime):
      raise EntityError('dateAssigned')
    self.dateAssigned = dateAssigned
    if (dateReviewed == None and type(dateReviewed) != datetime.datetime):
      raise EntityError('dateReviewed')
    self.dateReviewed = dateReviewed
    
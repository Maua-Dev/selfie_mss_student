from enum import Enum


class STATE(Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    IN_REVIEW = "IN_REVIEW"
    PENDING_REVIEW = "PENDING_REVIEW"

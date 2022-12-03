from enum import Enum

class REVIEW_STATE(Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    EXPIRED = "EXPIRED"
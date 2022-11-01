import abc
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class AutomaticReview(abc.ABC):
    automaticallyRejected: bool
    rejectionReason: REJECTION_REASON
    labels: list[Label]

    def __init__(self, automaticallyRejected: bool, rejectionReason: REJECTION_REASON, labels: list[Label]):

        if (automaticallyRejected == None or type(automaticallyRejected) != bool):
          raise EntityError('automaticallyRejected') 
        self.automaticallyRejected = automaticallyRejected

        if (rejectionReason == None or type(rejectionReason) != REJECTION_REASON):
          raise EntityError('rejectionReason')
        self.rejectionReason = rejectionReason

        if (len(labels) == 0 or type(labels) != list):
          raise EntityError('labels')
        self.labels = labels

       
import abc
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class AutomaticReview(abc.ABC):
    automaticallyRejected: bool
    rejectionReasons: list[REJECTION_REASON]
    labels: list[Label]

    def __init__(self, automaticallyRejected: bool, rejectionReasons: list[REJECTION_REASON], labels: list[Label]):

        if (automaticallyRejected == None or type(automaticallyRejected) != bool):
          raise EntityError('automaticallyRejected') 
        self.automaticallyRejected = automaticallyRejected


        if (rejectionReasons == None or type(rejectionReasons) != list):
              raise EntityError('rejectionReasons')
        elif not all(isinstance(reason, REJECTION_REASON) for reason in rejectionReasons):
              raise EntityError('rejectionReasons')

        self.rejectionReasons = rejectionReasons


        if (len(labels) == 0 or type(labels) != list):
          raise EntityError('labels')
        self.labels = labels

       
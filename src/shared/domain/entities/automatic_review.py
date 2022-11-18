import abc
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.controller_errors import MissingParameters

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


    def __repr__(self):
        return f"AutomaticReview(automaticallyRejected={self.automaticallyRejected}, rejectionReasons={self.rejectionReasons}, labels={self.labels})"

    @staticmethod
    def read_automatic_review(automaticReview: dict) -> "AutomaticReview": 
      try:
          labels = list()

          for label_dict in automaticReview["labels"]:
              label = Label(
                  name = label_dict['name'],
                  coords = {
                              "Width": float(label_dict['coords']['Width']),
                              "Height": float(label_dict['coords']['Height']),
                              "Left": float(label_dict['coords']["Left"]),
                              "Top": float(label_dict['coords']["Top"])
                          },
                  confidence= float(label_dict["confidence"]),
                  parents= label_dict["parents"]
              )
              labels.append(label)

          result = AutomaticReview(
              automaticallyRejected=automaticReview['automaticallyRejected'] == "True",
              rejectionReasons=[REJECTION_REASON[reason] for reason in automaticReview["rejectionReasons"]],
              labels=labels,
          )
          
          return result

      except KeyError as err:
          raise MissingParameters(f"{err}")
       
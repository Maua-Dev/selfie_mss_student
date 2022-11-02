from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.entities.label import Label
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError

def read_automatic_review(automaticReview: dict) -> AutomaticReview: 
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
            rejectionReason=REJECTION_REASON[automaticReview["rejectionReason"]],
            labels=labels,
        )
        
        return result

    except KeyError as err:
        raise MissingParameters(f"{err}")
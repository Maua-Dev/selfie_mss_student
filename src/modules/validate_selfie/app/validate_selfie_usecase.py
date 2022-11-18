from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.utils.validation_lists import ValidationLists
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.entities.automatic_review import AutomaticReview

class ValidateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, rekognitionResult: dict) -> AutomaticReview:
        
        if type(rekognitionResult) != dict:
            raise EntityError('rekognitionResult')
        
        allLabels = list()
        
        if rekognitionResult.get("Labels") is None:
            raise EntityError('rekognitionResult')

        names = set()
        parents = set()

        labels = rekognitionResult['Labels']
        for label in labels:
            if len(label["Instances"]) == 0 and float(label["Confidence"]) >= Label.MIN_CONFIDENCE:
                labelDict = dict()
                
                labelDict["name"] = label["Name"]
                names.add(labelDict["name"])
                
                labelDict["confidence"] = float(label["Confidence"])
                labelDict["coords"] = dict()
                labelDict["parents"] = [parent["Name"] for parent in label["Parents"]] 
                for parent in labelDict["parents"]:
                    parents.add(parent)
                
                allLabels.append(labelDict)
                
            elif len(label["Instances"]) == 1 and float(label["Confidence"]) >= Label.MIN_CONFIDENCE:
                labelDict = dict()
                
                labelDict["name"] = label["Name"]
                names.add(labelDict["name"])
                
                labelDict["confidence"] = float(label["Confidence"])
                labelDict["coords"] = label["Instances"][0]["BoundingBox"]
                labelDict["parents"] = [parent["Name"] for parent in label["Parents"]] 
                for parent in labelDict["parents"]:
                    parents.add(parent)
                    
                allLabels.append(labelDict)
    
            else:
                for instance in label["Instances"]:
                    if float(instance["Confidence"]) >= Label.MIN_CONFIDENCE:
                        labelDict = dict()
                        
                        labelDict["name"] = label["Name"]
                        names.add(labelDict["name"])
                        
                        labelDict["confidence"] = float(instance["Confidence"])
                        labelDict["parents"] = [parent["Name"] for parent in label["Parents"]] 
                        for parent in labelDict["parents"]:
                            parents.add(parent)
                            
                        labelDict["coords"] = instance["BoundingBox"]
                        
                        allLabels.append(labelDict)

        rejectionReasons = list()
        
        for name in names:
            if ValidationLists.OBJECTS_NOT_ALLOWED.get(name) is not None:
                rejectionReasons.append(ValidationLists.OBJECTS_NOT_ALLOWED.get(name))
        
        for parent in parents:
            if ValidationLists.PARENTS_NOT_ALLOWED.get(parent) is not None:
                rejectionReasons.append(ValidationLists.PARENTS_NOT_ALLOWED.get(parent))
                
        if set(ValidationLists.OBJECTS_REQUIRED.values()).issubset(names):
            rejectionReasons.extend([name for name in ValidationLists.OBJECTS_REQUIRED.values() if name not in names])
            
        if set(ValidationLists.PARENTS_REQUIRED.values()).issubset(parents):
            rejectionReasons.extend([name for name in ValidationLists.PARENTS_REQUIRED.values() if name not in names])
                
        automaticallyRejected = len(rejectionReasons) > 0
        
        rejectionReasons = list(set(rejectionReasons)) if automaticallyRejected else [REJECTION_REASON.NONE]
        

        labelsEntity = [Label(
            confidence=label["confidence"], coords=label["coords"], name=label["name"], parents=label["parents"]
        ) for label in allLabels]

        return AutomaticReview(
            automaticallyRejected=automaticallyRejected,
            rejectionReasons=rejectionReasons,
            labels=labelsEntity
        )
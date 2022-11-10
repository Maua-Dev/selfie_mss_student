from typing import Dict
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.utils.validation_lists import ValidationLists
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.label import Label
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON


class ValidateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, rekognitionResult: dict) -> Dict:
        
        if type(rekognitionResult) != dict:
            raise EntityError('rekognitionResult')
        
        allLabels = list()
        
        if rekognitionResult.get("Labels") is None:
            raise EntityError('rekognitionResult')

        labels = rekognitionResult['Labels']
        for label in labels:
            if len(label["Instances"]) == 0:
                labelDict = dict()
                
                labelDict["name"] = label["Name"]
                labelDict["confidence"] = label["Confidence"]
                labelDict["coords"] = []
                labelDict["parents"] = [parent["Name"] for parent in label["Parents"]] 
                
                allLabels.append(labelDict)
                
            elif len(label["Instances"]) == 1:
                labelDict = dict()
                
                labelDict["name"] = label["Name"]
                labelDict["confidence"] = label["Confidence"]
                labelDict["coords"] = label["Instances"][0]["BoundingBox"]
                labelDict["parents"] = [parent["Name"] for parent in label["Parents"]] 
                
                allLabels.append(labelDict)
    
            else:
                for instance in label["Instances"]:
                    labelDict = dict()
                    
                    labelDict["name"] = label["Name"]
                    labelDict["confidence"] = instance["Confidence"]
                    labelDict["parents"] = [parent["Name"] for parent in label["Parents"]] 
                    labelDict["coords"] = instance["BoundingBox"]
                    
                    allLabels.append(labelDict)

        validLabels = [label for label in allLabels if float(label["confidence"]) >= Label.MIN_CONFIDENCE]
        rejectionReasons = list()
        
        names = set([label["name"] for label in validLabels])
        parents = set([parent for parents in (label["parents"] for label in validLabels) for parent in parents])
 
        for name in names:
            if ValidationLists.OBJECTS_NOT_ALLOWED.get(name) is not None:
                rejectionReasons.append(ValidationLists.OBJECTS_NOT_ALLOWED.get(name).value)
        
        for parent in parents:
            if ValidationLists.PARENTS_NOT_ALLOWED.get(parent) is not None:
                rejectionReasons.append(ValidationLists.PARENTS_NOT_ALLOWED.get(parent).value)
                
        if not all(name in names for name in ValidationLists.OBJECTS_REQUIRED.keys()):
            rejectionReasons = rejectionReasons + [name.value for name in ValidationLists.OBJECTS_REQUIRED.values() if name not in names]
            
        if not all(name in names for name in ValidationLists.PARENTS_REQUIRED.keys()):
            rejectionReasons = rejectionReasons + [name.value for name in ValidationLists.PARENTS_REQUIRED.values() if name not in names]
                
        automaticallyRejected = len(rejectionReasons) > 0
        
        rejectionReasons = list(set(rejectionReasons)) if automaticallyRejected else [REJECTION_REASON.NONE.value]
        
        rejectionReasons.sort()

        return {
            "automaticallyRejected": automaticallyRejected,
            "rejectionReasons": rejectionReasons,
            "labels": validLabels
        }
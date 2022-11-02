from enum import auto
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.automatic_review import AutomaticReview
import datetime
import pytest

        
       
class Test_Selfie():
    def test_selfie(self):
        
        student = Student(
                ra="17090212",
                name="Monkey Guy",
                email="uuaa@floresta.com"
                
            )        
        
        dateCreated = datetime.datetime.now()
        
        selfie = Selfie (
                        student = student,
                        dateCreated= dateCreated,
                        url= "https://www.maua.br",
                        state= STATE.DECLINED,
                        idSelfie= 1,
                        rejectionReason = REJECTION_REASON.COVERED_FACE,
                        rejectionDescription = "Balaclava",
                        automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
        )
        
        assert type(selfie) == Selfie
        assert selfie.student == student
        assert selfie.dateCreated == dateCreated
        assert selfie.state == STATE.DECLINED
        assert selfie.rejectionReason == REJECTION_REASON.COVERED_FACE
        assert selfie.rejectionDescription == "Balaclava"
        assert selfie.automaticReview.automaticallyRejected == True        

    def test_selfie_error(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17.090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )

        
    def test_selfie_error_ra_int(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra=17090212,
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )
      
    def test_selfie_error_url_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateCreated= datetime.datetime.now(),
                url= None,
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )
        
    def test_selfie_error_state_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= "PENDING_REVIEW",
                idSelfie= 1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )
      
    def test_selfie_error_id_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= None,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )
        
    def test_selfie_error_id_invalid_str(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= "1",
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )

    def test_selfie_error_rejectionReason_str(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1,
                rejectionReason = "REJECTION_REASON.COVERED_FACE",
                rejectionDescription = "Balaclava",
                automaticReview = AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
            )

    def test_selfie_error_rejectionDescription_int(self):
        with pytest.raises(EntityError):
          selfie = Selfie(
                  student= Student(
                                  ra="17090212",
                                  name="Monkey Guy",
                                  email="uuaa@floresta.com"
                                  ),
                  dateCreated= datetime.datetime.now(),
                  url= "www.maua.br",
                  state= STATE.PENDING_REVIEW,
                  idSelfie= 1,
                  rejectionReason = REJECTION_REASON.COVERED_FACE,
                  rejectionDescription = 1,
                  automaticReview=AutomaticReview(
  automaticallyRejected = True,
  rejectionReason = REJECTION_REASON.COVERED_FACE,
  labels = [Label(
      name="Brown Hair",
      coords={},
      confidence=98.979095458984383,
      parents=[],
    ), 
    Label(
      name="Glasses",
      coords={
        "Width": 0.6591288447380066,
        "Height": 0.17444363236427307,
        "Left": 0.19148917496204376,
        "Top": 0.3813813030719757
          },
      confidence=94.5357666015625,
      parents=["Accessories"],
    ),
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
        )]
)
              )
        
    def test_selfie_error_id_invalid_negative(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= -1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview=AutomaticReview(
                                                automaticallyRejected = True,
                                                rejectionReason = REJECTION_REASON.COVERED_FACE,
                                                labels = [Label(
                                                    name="Brown Hair",
                                                    coords={},
                                                    confidence=98.979095458984383,
                                                    parents=[],
                                                  ), 
                                                  Label(
                                                    name="Glasses",
                                                    coords={
                                                      "Width": 0.6591288447380066,
                                                      "Height": 0.17444363236427307,
                                                      "Left": 0.19148917496204376,
                                                      "Top": 0.3813813030719757
                                                        },
                                                    confidence=94.5357666015625,
                                                    parents=["Accessories"],
                                                  ),
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
                                                      )]
                                                    )
        )
      
    def test_selfie_error_automatic_review_empty(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateCreated= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= -1,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Balaclava",
                automaticReview="Salve do beck"
        )
      
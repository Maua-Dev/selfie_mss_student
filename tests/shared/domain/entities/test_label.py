from src.shared.domain.entities.label import Label
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_Label():
    def test_Label(self):
        
        label = Label(
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents="",
        )
        
        
        assert label.name == "Person"
        assert label.coords == {
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  }
        assert label.confidence == 98.54370880126953
        assert label.parents == ""

    def test_Label_error_int_name(self):
      with pytest.raises(EntityError):
        label = Label(
          name=1,
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents="",
        )

        
    def test_Label_error_str_confidance(self):
      with pytest.raises(EntityError):
        label = Label(
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence="98.54370880126953",
          parents="",
        )
      
    def test_Label_error_int_parent(self):
      with pytest.raises(EntityError):
        label = Label(
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents=1,
        )

    def test_Label_error_int_coords(self):
      with pytest.raises(EntityError):
        label = Label(
          name="Person",
          coords=1,
          confidence=98.54370880126953,
          parents="",
        )
    
    def test_Label_error_none_name(self):
      with pytest.raises(EntityError):
        label = Label(
          name=None,
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=98.54370880126953,
          parents="",
        )

    def test_Label_error_none_confidance(self):
      with pytest.raises(EntityError):
        label = Label(
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=None,
          parents="",
        )

    def test_lable_error_min_confidance(self):
      with pytest.raises(EntityError):
        label = Label(
          name="Person",
          coords={
                    "Width": 0.9711952805519104,
                    "Height": 0.8659809827804565,
                    "Left": 0.012313545681536198,
                    "Top": 0.11108686774969101
                  },
          confidence=89.54370880126953,
          parents="",
        )
    
    def test_lable_error_none_coords_parents(self):
        label = Label(
          name="Person",
          coords=None,
          confidence=98.54370880126953,
          parents=None,
        )
        assert label.name == "Person"
        assert label.coords == None
        assert label.confidence == 98.54370880126953
        assert label.parents == None

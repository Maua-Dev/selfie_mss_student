
class RequestUploadSelfieViewModel:
    presignedPost: dict

    def __init__(self, presignedPost: dict):
      self.presignedPost = presignedPost

    def to_dict(self) -> dict:
        return self.presignedPost
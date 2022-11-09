
class RequestUploadSelfieViewModel:
    presigned_post: dict

    def __init__(self, presigned_post: dict):
      self.presigned_post = presigned_post

    def to_dict(self) -> dict:
        return self.presigned_post
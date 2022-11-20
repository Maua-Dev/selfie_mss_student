from datetime import datetime
import uuid
from src.shared.domain.repositories.selfie_repository_interface import ISelfieRepository
import boto3
from src.shared.environments import Environments

class SelfieRepositoryS3(ISelfieRepository):
    S3_BUCKET_NAME: str

    def __init__(self):
        self.S3_BUCKET_NAME = Environments.get_envs().s3_bucket_name
        self.s3_client = boto3.client('s3')

      
    def generate_uuid_key(self, ra: str):

        key = f"{ra}/selfie-{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}-{str(uuid.uuid4())[:5]}.jpeg"
        return key


    def request_upload_selfie(self, ra: str, name: str, email: str) -> dict:
        key = self.generate_uuid_key(ra=ra)
  
        meta = {
            "x-amz-meta-ra": ra,
            "x-amz-meta-name": name,
            "x-amz-meta-email": email
        }

        try:
            print("Trying to upload file to S3")
            presignedPost = self.s3_client.generate_presigned_post(
            Bucket=self.S3_BUCKET_NAME,
            Key=key,
            Fields=meta,
            Conditions=[{key: value} for (key, value) in meta.items()],
            ExpiresIn=600
            )
        except Exception as e:
            print("Error while trying to upload file to S3")
            print(e)
            raise e

        return presignedPost
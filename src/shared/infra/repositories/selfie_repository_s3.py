from datetime import datetime
import uuid
from src.shared.domain.repositories.selfie_repository_interface import ISelfieRepository
import boto3
from botocore.config import Config
from src.shared.environments import Environments

class SelfieRepositoryS3(ISelfieRepository):
    S3_BUCKET_NAME: str

    def __init__(self):
        self.S3_BUCKET_NAME = Environments.get_envs().s3_bucket_name
        self.s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))

      
    def generate_uuid_key(self, ra: str):

        key = f"{ra}/selfie-{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}-{str(uuid.uuid4())[:5]}.jpeg"
        return key


    def request_upload_selfie(self, ra: str, name: str, email: str) -> dict:
        key = self.generate_uuid_key(ra=ra)
  
        meta = {
            "ra": ra,
            "name": name,
            "email": email
        }

        try:
            presignedUrl = self.s3_client.generate_presigned_url(
                ClientMethod='put_object',
                Params={
                    'Bucket': self.S3_BUCKET_NAME,
                    'Key': key,
                    'Metadata': meta,
                },
                ExpiresIn=600,
            )

        except Exception as e:
            print("Error while trying to upload file to S3")
            print(e)
            raise e

        return {
            "url": presignedUrl,
            "metadata": meta
        }
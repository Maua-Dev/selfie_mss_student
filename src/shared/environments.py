import enum
from enum import Enum
import os




class STAGE(Enum):
    LOCAL = "LOCAL"
    DEV = "DEV"
    PROD = "PROD"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    s3_bucket_name: str
    region: str
    endpoint_url: str = None


    def _configure_local(self):
        from dotenv import load_dotenv
        os.environ["STAGE"] = STAGE.LOCAL.value
        load_dotenv()

    def load_envs(self):
        if "STAGE" not in os.environ:
            self._configure_local()

        self.stage = os.environ.get("STAGE")
        self.s3_bucket_name = os.environ.get("S3_BUCKET_NAME")
        self.region = os.environ.get("REGION")
        self.endpoint_url = os.environ.get("ENDPOINT_URL")

    def __repr__(self):
        return (
            f"Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})"
        )

    @staticmethod
    def __call__() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs


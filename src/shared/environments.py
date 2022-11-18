import enum
from enum import Enum
import os




class STAGE(Enum):
    LOCAL = "LOCAL"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    s3_bucket_name: str
    region: str
    endpoint_url: str = None
    dynamo_table_name: str
    dynamo_partition_key: str
    dynamo_sort_key: str


    def _configure_local(self):
        from dotenv import load_dotenv
        os.environ["STAGE"] = STAGE.LOCAL.value
        load_dotenv()

    def load_envs(self):
        if "STAGE" not in os.environ:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

        if self.stage == STAGE.TEST:
            self.s3_bucket_name = "bucket-test"
            self.region = "us-east-1"
            self.endpoint_url = "http://localhost:8000"
            self.dynamo_table_name = "selfie_mss_student-table"
            self.dynamo_partition_key = "PK"
            self.dynamo_sort_key = "SK"
        else:
            self.s3_bucket_name = os.environ.get("S3_BUCKET_NAME")
            self.region = os.environ.get("REGION")
            self.endpoint_url = os.environ.get("ENDPOINT_URL")
            self.dynamo_table_name = os.environ.get("DYNAMO_TABLE_NAME")
            self.dynamo_partition_key = os.environ.get("DYNAMO_PARTITION_KEY")
            self.dynamo_sort_key = os.environ.get("DYNAMO_SORT_KEY")

    def __repr__(self):
        return f"Environments(stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url}, dynamo_table_name={self.dynamo_table_name}, dynamo_partition_key={self.dynamo_partition_key}, dynamo_sort_key={self.dynamo_sort_key})"


    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs


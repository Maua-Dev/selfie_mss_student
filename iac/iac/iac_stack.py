from aws_cdk import (
    Stack,
)
from aws_cdk.aws_apigateway import RestApi, Cors
from constructs import Construct

from .dynamo_stack import DynamoStack
from .lambda_stack import LambdaStack


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.rest_api = RestApi(self, "Selfie_RestApi",
                                rest_api_name="Selfie_RestApi",
                                description="This is the Selfie RestApi",
                                default_cors_preflight_options=
                                {
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
                                )

        mss_student_api_resource = self.rest_api.root.add_resource("mss-student", default_cors_preflight_options=
        {
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
                                                                   )

        self.dynamo_stack = DynamoStack(self, "DynamoStack")

        ENVIRONMENT_VARIABLES = {
            "REGION": "sa-east-1",
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            "DYNAMO_PARTITION_KEY": self.dynamo_stack.dynamo_table.partition_key.name,
            "DYNAMO_SORT_KEY": self.dynamo_stack.dynamo_table.sort_key.name
        }

        self.lambda_stack = LambdaStack(self, mss_student_api_resource=mss_student_api_resource, environment_variables=ENVIRONMENT_VARIABLES)

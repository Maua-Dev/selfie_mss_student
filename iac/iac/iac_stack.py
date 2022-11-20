from aws_cdk import (
    Stack, CfnOutput
)
from aws_cdk.aws_apigateway import RestApi, Cors
from constructs import Construct

from .dynamo_stack import DynamoStack
from .lambda_stack import LambdaStack
from .selfie_repository_stack import SelfieRepositoryStack


class IacStack(Stack):
    dynamo_stack: DynamoStack
    lambda_stack: LambdaStack
    selfie_repository_stack: SelfieRepositoryStack

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
            "STAGE": "DEV",
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            "DYNAMO_PARTITION_KEY": self.dynamo_stack.partition_key_name,
            "DYNAMO_SORT_KEY": self.dynamo_stack.sort_key_name
        }

        self.lambda_stack = LambdaStack(self, mss_student_api_resource=mss_student_api_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES)

        for func in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table.grant_read_write_data(func)

        self.selfie_repository_stack = SelfieRepositoryStack(self, "SelfieRepositoryStack", create_selfie_lambda_function=self.lambda_stack.create_selfie_function, validate_selfie_lambda_function=self.lambda_stack.validate_selfie_function)



        self.lambda_stack.request_upload_selfie_function.add_environment("S3_BUCKET_NAME", self.selfie_repository_stack.s3_bucket.bucket_name)
        self.selfie_repository_stack.s3_bucket.grant_read(self.lambda_stack.request_upload_selfie_function)
        self.selfie_repository_stack.s3_bucket.grant_write(self.lambda_stack.request_upload_selfie_function)


        output_1 = CfnOutput(self, "S3 Bucket Name",
                                value=self.selfie_repository_stack.s3_bucket.bucket_name,
                                description="S3 Bucket Name",
                                export_name="S3BucketName"
                                )

        output_2 = CfnOutput(self, "Dynamo Table Name",
                                value=self.dynamo_stack.dynamo_table.table_name,
                                description="Dynamo Table Name",
                                export_name="DynamoTableName"
                                )

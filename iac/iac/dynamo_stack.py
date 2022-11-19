from aws_cdk import (
    aws_dynamodb as dynamodb,
    NestedStack,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class DynamoStack(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.dynamo_table = dynamodb.Table(self, "Selfie_Dynamo_Table",
                                             partition_key=dynamodb.Attribute(name="PK",
                                                                                type=dynamodb.AttributeType.STRING),
                                                sort_key=dynamodb.Attribute(name="SK",
                                                                            type=dynamodb.AttributeType.STRING),
                                                billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
                                                )



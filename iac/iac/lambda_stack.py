from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class LambdaStack(NestedStack):

    def __init__(self, scope: Construct, mss_student_api_resource: Resource) -> None:
        super().__init__(scope, "Selfie_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "Selfie_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )

        self.get_student = lambda_.Function(
            self, "Get_Student",
            code=lambda_.Code.from_asset("../src/modules/get_student"),
            handler="app.get_student_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer]
        )

        mss_student_api_resource.add_resource("get-student").add_method("GET", integration=LambdaIntegration(self.get_student))







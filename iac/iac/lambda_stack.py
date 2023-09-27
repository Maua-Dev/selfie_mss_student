from typing import List

from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration, Stack
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class LambdaStack(Construct):

    functions_that_need_dynamo_permissions = []
    layers: List[lambda_.LayerVersion]

    def createLambdaApiGatewayIntegration(self, module_name: str, method: str, mss_student_api_resource: Resource, environment_variables: dict = {"STAGE": "TEST"}):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=self.lambda_layer,
            environment=environment_variables,
            timeout=Duration.seconds(15),
            tracing=lambda_.Tracing.ACTIVE
        )

        mss_student_api_resource.add_resource(module_name.replace("_", "-")).add_method(method,
                                                                                        integration=LambdaIntegration(
                                                                                            function))

        return function

    def __init__(self, scope: Construct, mss_student_api_resource: Resource, environment_variables: dict) -> None:
        super().__init__(scope, "Selfie_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "Selfie_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )

        # self.lambda_power_tools_layer = lambda_.LayerVersion.from_layer_version_arn(
        #     self, "Lambda_Power_Tools_Layer",
        #     layer_version_arn=f"arn:aws:lambda:{Stack.of(self).region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:15"
        # )
        #
        #
        #
        # self.layers = [self.lambda_layer, self.lambda_power_tools_layer]



        self.get_student_function = self.createLambdaApiGatewayIntegration(
            module_name="get_student",
            method="GET",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.create_student_function = self.createLambdaApiGatewayIntegration(
            module_name="create_student",
            method="POST",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.update_student_function = self.createLambdaApiGatewayIntegration(
            module_name="update_student",
            method="POST",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.delete_student_function = self.createLambdaApiGatewayIntegration(
            module_name="delete_student",
            method="POST",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )

        self.get_selfie_function = self.createLambdaApiGatewayIntegration(
            module_name="get_selfie",
            method="GET",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.get_selfies_by_ra_function = self.createLambdaApiGatewayIntegration(
            module_name="get_selfies_by_ra",
            method="GET",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.update_selfie_function = self.createLambdaApiGatewayIntegration(
            module_name="update_selfie",
            method="POST",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.delete_selfie_function = self.createLambdaApiGatewayIntegration(
            module_name="delete_selfie",
            method="POST",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.get_all_selfies_function = self.createLambdaApiGatewayIntegration(
            module_name="get_all_selfies",
            method="GET",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables,
        )
        self.get_all_students_function = self.createLambdaApiGatewayIntegration(
            module_name="get_all_students",
            method="GET",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )
        self.request_upload_selfie_function = self.createLambdaApiGatewayIntegration(
            module_name="request_upload_selfie",
            method="POST",
            mss_student_api_resource=mss_student_api_resource,
            environment_variables=environment_variables
        )


        self.create_selfie_function = lambda_.Function(
            self, "create_selfie",
            code=lambda_.Code.from_asset(f"../src/modules/create_selfie"),
            handler=f"app.create_selfie_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=self.lambda_layer,
            environment=environment_variables,
            timeout=Duration.seconds(15),
            tracing=lambda_.Tracing.ACTIVE
        )
        self.validate_selfie_function = lambda_.Function(
            self, "validate_selfie",
            code=lambda_.Code.from_asset(f"../src/modules/validate_selfie"),
            handler=f"app.validate_selfie_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=self.lambda_layer,
            environment=environment_variables,
            timeout=Duration.seconds(15),
            tracing=lambda_.Tracing.ACTIVE
        )

        self.functions_that_need_dynamo_permissions = [
            self.get_student_function,
            self.create_student_function,
            self.update_student_function,
            self.delete_student_function,
            self.get_selfie_function,
            self.get_selfies_by_ra_function,
            self.create_selfie_function,
            self.validate_selfie_function,
            self.update_selfie_function,
            self.delete_selfie_function,
            self.get_all_selfies_function,
            self.get_all_students_function,
            self.request_upload_selfie_function
        ]



from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration


class LambdaStack(NestedStack):

    def createLambdaApiGatewayIntegration(self, module_name: str, method: str, mss_student_api_resource: Resource, enviroment_variables: dict = {"STAGE": "TEST"}):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            environment=enviroment_variables,
            timeout=Duration.seconds(15)
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

        self.get_student_function = self.createLambdaApiGatewayIntegration(module_name="get_student", method="GET", mss_student_api_resource=mss_student_api_resource)
        self.create_student_function = self.createLambdaApiGatewayIntegration(module_name="create_student", method="POST", mss_student_api_resource=mss_student_api_resource)
        self.update_student_function = self.createLambdaApiGatewayIntegration(module_name="update_student", method="POST", mss_student_api_resource=mss_student_api_resource)
        self.delete_student_function = self.createLambdaApiGatewayIntegration(module_name="delete_student", method="POST", mss_student_api_resource=mss_student_api_resource)

        self.get_selfie_function = self.createLambdaApiGatewayIntegration(module_name="get_selfie", method="GET", mss_student_api_resource=mss_student_api_resource)
        self.get_selfies_by_ra_function = self.createLambdaApiGatewayIntegration(module_name="get_selfies_by_ra", method="GET", mss_student_api_resource=mss_student_api_resource,
                                               enviroment_variables=environment_variables)
        self.create_selfie_function = self.createLambdaApiGatewayIntegration(module_name="create_selfie", method="POST", mss_student_api_resource=mss_student_api_resource)
        self.update_selfie_function = self.createLambdaApiGatewayIntegration(module_name="update_selfie", method="POST", mss_student_api_resource=mss_student_api_resource)
        self.delete_selfie_function = self.createLambdaApiGatewayIntegration(module_name="delete_selfie", method="POST", mss_student_api_resource=mss_student_api_resource)
        self.get_all_selfies_function = self.createLambdaApiGatewayIntegration(module_name="get_all_selfies", method="GET", mss_student_api_resource=mss_student_api_resource,
                                               enviroment_variables=environment_variables)
        self.get_all_students_function = self.createLambdaApiGatewayIntegration(module_name="get_all_students", method="GET", mss_student_api_resource=mss_student_api_resource)



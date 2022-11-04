from aws_cdk import (
    aws_s3 as aws_s3,
    aws_ecr,
    aws_codebuild,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpactions,
    pipelines,
    aws_secretsmanager as secretsmanager,
    aws_ssm,
    App, Aws, CfnOutput, Duration, RemovalPolicy, Stack
)

from iac.iac_stack import IacStack


class PipelineStack(Stack):
    def __init__(self, app: App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        codePipeline = pipelines.CodePipeline(self, 'CodePipeline',
                                              pipeline_name='SelfieMssStudentPipeline',
                                              synth=pipelines.ShellStep('Synth',
                                                                        input=pipelines.CodePipelineSource.connection(
                                                                            repo_string='Maua-Dev/selfie_mss_student',
                                                                            connection_arn='arn:aws:codestar-connections:sa-east-1:264055331071:connection/9c698ffc-0710-4643-b3f6-45e862e1ae2c',
                                                                            branch='cd-pipeline'),
                                                                        commands=[
                                                                            'cd iac',
                                                                            'python -m pip install -r requirements.txt',
                                                                            'npx cdk synth',
                                                                        ],
                                                                        primary_output_directory='iac/cdk.out'
                                                                        )
                                              )

        # pre_prod_app = IacStack(self, 'Pre-Prod', env={
        #     'account': '264055331071',
        #     'region': 'eu-central-1',
        # })
        # pre_prod_stage = codePipeline.add_application_stage(pre_prod_app)

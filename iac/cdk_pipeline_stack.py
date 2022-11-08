from aws_cdk import (
    pipelines,
    App, Stack
)

from iac.pipeline_stage import PipelineStage

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

        codePipeline.add_stage(PipelineStage(self, 'Dev'))

        # pre_prod_app = IacStack(self, 'Pre-Prod', env={
        #     'account': '264055331071',
        #     'region': 'eu-central-1',
        # })






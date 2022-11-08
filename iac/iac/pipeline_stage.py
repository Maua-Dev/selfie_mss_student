from aws_cdk import (
    Stage
)
from constructs import Construct

from .iac_stack import IacStack


class PipelineStage(Stage):

    def __init__(self, scope: Construct, stage_name: str,  **kwargs) -> None:
        super().__init__(scope, stage_name, **kwargs)

        mss_selfie_student = IacStack(self, "MssSelfieStudent")


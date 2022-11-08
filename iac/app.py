#!/usr/bin/env python3
import os

import aws_cdk as cdk

from adjust_layer_directory import adjust_layer_directory
from iac.iac_stack import IacStack
from cdk_pipeline_stack import PipelineStack

print("Starting the CDK")

print("Adjusting the layer directory")
adjust_layer_directory(shared_dir_name="shared", destination="lambda_layer_out_temp")
print("Finished adjusting the layer directory")


env = {
    "account": os.environ["AWS_ACCOUNT_ID"],
    "region": "sa-east-1"
}

app = cdk.App()

IacStack(app, "IacStack", env=env)
# PipelineStack(app, "PipelineStack", env=env)


app.synth()

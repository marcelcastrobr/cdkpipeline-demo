#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_pipeline_demo.webservice_stack import WebServiceStack
from cdk_pipeline_demo.pipeline_stack import MyPipelineStack

PIPELINE_ACCOUNT = '656001362760'

app = cdk.App()
MyPipelineStack(app, 'PipelineStack',
    env={
        'account': PIPELINE_ACCOUNT,
        'region': 'eu-central-1'
    })
app.synth()

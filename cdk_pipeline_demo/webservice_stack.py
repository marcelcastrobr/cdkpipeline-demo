from os import path
import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lmb,
    aws_apigateway as apigw,
)
from constructs import Construct

class WebServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        this_dir = path.dirname(__file__)

        handler = lmb.Function(self, 'Handler',
            runtime=lmb.Runtime.PYTHON_3_7,
            handler='handler.handlers',
            code=lmb.Code.from_asset(path.join(this_dir,'lambda'))
            )

        gw = apigw.LambdaRestApi(self, 'Gateway',
            description='Endpoint for a simple Lambda-powered web service',
            handler=handler
        )

        self.url_output = cdk.CfnOutput(self, 'Url',
            value=gw.url)

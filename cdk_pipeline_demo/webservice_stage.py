import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    # Duration,
    Stage
)

from .webservice_stack import WebServiceStack

class MyWebservice(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None: 
        super().__init__(scope, construct_id, **kwargs)

        my_service = WebServiceStack(self, "WebService")
        self.url_output = my_service.url_output


import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
)

from .webservice_stage import MyWebservice

class MyPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None: 
        super().__init__(scope, construct_id, **kwargs)

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep("Synth",
            input=pipelines.CodePipelineSource.git_hub("marcelcastrobr/cdkpipeline-demo", "main",
                authentication=cdk.SecretValue.secrets_manager("github-secret")),
            install_commands=["pip install -r requirements.txt"],
            commands=["pytest unittests", "npx cdk synth"]))


        my_app_preprod = MyWebservice(self, "Pre-prod", env=cdk.Environment(
            account='558679333679',
            region='eu-central-1'
        ) )
        pipeline.add_stage(my_app_preprod,
            post=[pipelines.ShellStep("Validate Endpoint",
            env_from_cfn_outputs={"URL": my_app_preprod.url_output},
            commands=["pip install -r requirements.txt", "pytest integtests"])])

        pipeline.add_stage(MyWebservice(self, "Production", env=cdk.Environment(
            account='558679333679',
            region='eu-central-1'
        ) ),
        ## Adding manual approval
        #pre=[pipelines.ManualApprovalStep("PromoteToProd")]
        )
    


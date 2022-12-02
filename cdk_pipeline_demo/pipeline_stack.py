import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
)

class MyPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None: 
        super().__init__(scope, construct_id, **kwargs)

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep("Synth",
            input=pipelines.CodePipelineSource.git_hub("marcelcastrobr/cdkpipeline-demo", "main",
                authentication=cdk.SecretValue.secrets_manager("github-token")),
                install_commands=["pip install -r requirements.txt"],
                commands=["npx cdk synth"]))
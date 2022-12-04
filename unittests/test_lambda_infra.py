import aws_cdk as cdk
from cdk_pipeline_demo.webservice_stack import WebServiceStack


def test_lambda_handler():
    # GIVEN
    app = cdk.App()

    # WHEN
    WebServiceStack(app, 'Stack')

    # THEN
    template = app.synth().get_stack_by_name('Stack').template
    functions = [resource for resource in template['Resources'].values()
                if resource['Type'] == 'AWS::Lambda::Function'
    ]
    assert len(functions) == 1
    assert functions[0]['Properties']['Handler'] == 'handler.handler'
from aws_cdk import aws_s3 as s3, RemovalPolicy
from constructs import Construct

class S3Construct(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        s3.Bucket(
            self,
            "MyBucket",
            bucket_name="bucket100524-using-python-cdk",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY
        )

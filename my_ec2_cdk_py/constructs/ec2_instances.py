from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class Ec2InstanceConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        vpc: ec2.Vpc,
        security_group: ec2.SecurityGroup,
        name: str,
        public: bool,
        instance_type: str = "t2.micro",
        key_name: str | None = None
    ):
        super().__init__(scope, id)

        self.instance = ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType(instance_type),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
                if public else ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            security_group=security_group,
            key_name="cli-user" if public else None
        )

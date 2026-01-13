from aws_cdk import aws_ec2 as ec2, CfnOutput
from constructs import Construct

class Ec2InstanceConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        vpc: ec2.Vpc,
        security_group: ec2.SecurityGroup,
        instance_config: dict
    ):
        super().__init__(scope, id)

        name = instance_config["name"]
        public = instance_config["public"]

        vpc_subnets = (
            ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
            if public else None
        )

        sg = security_group if public else None
        key_name = "cli-user" if public else None

        instance = ec2.Instance(
            self,
            f"{name}-instance",
            vpc=vpc,
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            vpc_subnets=vpc_subnets,
            security_group=sg,
            key_name=key_name
        )

        if public:
            CfnOutput(
                self,
                f"{name}_PublicIp",
                value=instance.instance_public_ip
            )

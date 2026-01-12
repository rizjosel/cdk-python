from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
)
from constructs import Construct


class MyEc2CdkPyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # 🔹 VPC (Free Tier safe)
        vpc = ec2.Vpc(
            self,
            "FreeTierVpc",
            max_azs=2,
            nat_gateways=0
        )

        # 🔹 Security Group (SSH only)
        sg = ec2.SecurityGroup(
            self,
            "FreeTierSG",
            vpc=vpc,
            description="Allow SSH access",
            allow_all_outbound=True
        )

        sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH"
        )

        # 🔹 EC2 Instance (Free Tier)
        instance = ec2.Instance(
            self,
            "FreeTierInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=sg,
            key_name="cli-user"  # 🔑 must exist in this region
        )

        # 🔹 Outputs
        CfnOutput(self, "InstanceId", value=instance.instance_id)
        CfnOutput(self, "PublicIp", value=instance.instance_public_ip)


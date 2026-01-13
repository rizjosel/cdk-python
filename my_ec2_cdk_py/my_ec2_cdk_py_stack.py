from aws_cdk import Stack
from constructs import Construct
from my_ec2_cdk_py.constructs.vpc_sg import VpcConstruct
from my_ec2_cdk_py.constructs.s3_bucket import S3Construct
from my_ec2_cdk_py.constructs.ec2_instances import Ec2InstanceConstruct

class MyEc2CdkPyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, config: dict, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        if config.get("enable_s3"):
            S3Construct(self, "S3")

        vpc_construct = VpcConstruct(self, "Vpc")

        for inst in config.get("instances", []):
            Ec2InstanceConstruct(
                self,
                f"{inst['name']}-Ec2",
                vpc=vpc_construct.vpc,
                security_group=vpc_construct.security_group,
                instance_config=inst
            )





"""""
        name = ["bucket1","bucket2","bucket3"]

        for i in name:
            s3.Bucket(
                self,
                f"{i}",
                bucket_name=f"{i}-using-python-cdk"
            )

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
"""""
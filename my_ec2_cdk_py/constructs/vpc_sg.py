from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class VpcConstruct(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        self.vpc = ec2.Vpc(
            self,
            "FreeTierVpc",
            max_azs=2,
            nat_gateways=0
        )

        self.security_group = ec2.SecurityGroup(
            self,
            "FreeTierSG",
            vpc=self.vpc,
            description="Allow SSH access",
            allow_all_outbound=True
        )

        self.security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH"
        )

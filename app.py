#!/usr/bin/env python3
import os
import aws_cdk as cdk
from my_ec2_cdk_py.my_ec2_cdk_py_stack import MyEc2CdkPyStack
from my_ec2_cdk_py.config import CONFIG


app = cdk.App()
MyEc2CdkPyStack(app, "MyEc2CdkPyStack", config=CONFIG)
app.synth()

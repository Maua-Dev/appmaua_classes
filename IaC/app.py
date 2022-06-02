#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iac.iac_stack import AppMauaBack

env_TEMP = cdk.Environment(account="171487071332", region="us-east-1")



app = cdk.App()
AppMauaBack(app, "IaCStack", env=cdk.Environment())

app.synth()

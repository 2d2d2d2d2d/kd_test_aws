#!/usr/bin/env python3
import os

import aws_cdk as cdk

from project_folder.project_folder_stack import ProjectFolderStack


app = cdk.App()
ProjectFolderStack(app, "Hello world")
app.synth()

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from setuptools import setup

setup(
    name="aws_doc_sdk_examples_tools",
    version="0.0.1",
    packages=["aws_doc_sdk_examples_tools"],
    install_requires=[
        "pathspec==0.11.2",
        "PyYAML==6.0.1",
        "yamale==4.0.4",
    ],
)
import os
import re
import sys
from setuptools import setup, find_packages
from _version import __VERSION__

sys.path.append("./prettydata")
sys.path.append("./tests")
with open("requirements.txt") as requirements_file:
    install_requirements = requirements_file.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="PrettyData",
    version=__VERSION__,
    description="Cleansing the data to use with analyzing task",
    long_description=long_description,
    author="Yusuke Kambara",
    license="MIT",

    packages=find_packages("prettydata"),
    package_dir={"": "prettydata"},
    test_suite = "tests.test.suite",
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "prettydata=prettydata.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ]
)
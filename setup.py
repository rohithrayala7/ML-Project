from setuptools import setup,find_packages
from typing import List


#declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="rohith_rayala"
DESCRIPTION="This is a first regression project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    This func will return list of requirements mentioned in requirement.txt file.
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #["housing"]
install_requires=get_requirements_list()

)

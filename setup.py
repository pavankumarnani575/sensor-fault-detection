from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """This functio will return list of requirements

    Returns:
        List[str]: _description_
    """
    requirements_list :List[str] = []
    return requirements_list

setup(

    name = "sensor",
    version="0.0.1",
    author = "pavan",
    author_email = "pavankumarnani575@gmail.com",
    packages =find_packages(),
    install_requires = get_requirements(),
)
from setuptools import setup,find_packages
from typing import List

hypen_e ="-e ."

def get_packages(path):
    requirements=[]
    with open(path) as path:
        requirements=path.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e in requirements:
            requirements.remove(hypen_e)


setup(
    name="Restaurant_Rating_Prediction",
    version="0.1",
    author="ehetsham",
    author_email="ehetsham.s@gmail.com",
    install_requires=get_packages("requirements.txt"),
    packages=find_packages()
)
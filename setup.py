from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Famous Figure Recognition and Generative Q&A Engine",
    version="0.1",
    author="Prakash",
    packages=find_packages(),
    install_requires = requirements,
)
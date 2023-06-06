from setuptools import setup

# Read the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='vulnerable.ai',
    version='1.0',
    description='Find bugs in Smart Contracts',
    author='Shivam Arora',
    author_email='arorashivam@protonmail.com.com',
    packages=['/'],
    install_requires=requirements,
)

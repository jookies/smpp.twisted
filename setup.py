import os
from setuptools import setup, find_packages


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and (not line.startswith("#") and not line.startswith('-'))]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="smpp.twisted3",
    version="0.7",
    author="Roger Hoover",
    author_email="roger.hoover@gmail.com",
    description="SMPP 3.4 client built on Twisted / Python3",
    license='Apache License 2.0',
    packages=find_packages(exclude=["tests"]),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords="smpp twisted",
    url="https://github.com/jookies/smpp.twisted",
    py_modules=["smpp.twisted3"],
    include_package_data=True,
    package_data={'smpp.twisted3': ['README.md']},
    zip_safe=False,
    install_requires=parse_requirements('requirements.txt'),
    tests_require=[
        'mock',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Twisted",
        "Topic :: System :: Networking",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

import runpy
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

VERSION = runpy.run_path(
    os.path.join(here, "pysimulator", "version.py")
)["VERSION"]


def read_requirements(name):
    with open(os.path.join(here, name), encoding='utf-8') as f:
        require_str = f.read()
        return require_str.split()

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysimulator',
    version=VERSION,
    packages=['pysimulator'],
    url='https://github.com/youngfeeFJS/pysimulator.git',
    author='youngfreeFJS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS",
    ],
    entry_points={},
    install_requires=read_requirements('requirements.txt'),
    extras_require={
        'dev': read_requirements('requirements.dev.txt')
    }
)

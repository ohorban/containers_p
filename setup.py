import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_ohorban_container",
    version="0.0.1",
    description="Data structures: BST, AVL, Heap, unicode",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ohorban/containers_p",
    author="Alex Horban",
    author_email="20ohorban@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=[],
)

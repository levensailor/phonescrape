import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phonescrape",
    version="0.0.1",
    author="Jeff Levensailor",
    author_email="jeff@levensailor.com",
    description="Downloads and parses information from Cisco IP Phones",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/levensailor/phonescrape",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
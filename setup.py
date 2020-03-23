import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swingby", # Replace with your own username
    version="1.0.0",
    author="Jacob Samuel",
    author_email="jacob@swingby.network",
    description="Swingby developer tools for Python 3",
    long_description=long_description,
    url="https://github.com/SwingbyProtocol/python-sdk.git",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

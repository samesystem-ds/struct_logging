import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="struct_logging",
    version="0.0.1",
    author="SameSystem",
    author_email="linas.ziedas@samesystem.com",
    description="Struct logging for apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samesystem-ds/struct_logging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

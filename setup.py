import setuptools
import versioneer

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="softnanotools",
    author="Debesh Mandal",
    description="Tools for computing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softnanolab/softnanotools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)

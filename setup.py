import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fr:
    requires = fr.read().strip().split('\n')


setuptools.setup(
    name="gryphon-analytics-basic",
    version="0.0.23",
    author="Daniel Wang",
    author_email="daniel.wang@oliverwyman.com",
    description="A public github-hosted python package for test, with dependency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ow-gryphon/gryphon-analytics-basic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requires,
)

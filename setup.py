import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textColor",
    version="0.0.1",
    author="Jannik Ramrath",
    author_email="jannik.ramrath@gmail.com",
    description="The purpose of this Library is to add easy acces to colored output in the Terminal with Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/R2-D2-JR/textColor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

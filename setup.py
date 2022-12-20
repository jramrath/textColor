import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textColor",
    version="2.0.2",
    author="Jannik Ramrath",
    author_email="textcolor@ramrath.anonaddy.me",
    description="This is an easy to use Python library which allows you to make your terminal outputs more colorful and therefore easier to read and understand",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jramrath/textColor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    test_require=['pytest>=4.4.1'],
    test_suit='test'
)

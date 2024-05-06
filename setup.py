from os import chdir
from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup

with open(join(dirname(__file__), "README.md")) as readme:
    README = readme.read()


# allow setup.py to be run from any path
chdir(normpath(abspath(dirname(__file__))))

import dj_svg  # noqa

setup(
    name="dj-svg",
    version=dj_svg.__version__,
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    license=dj_svg.__license__,
    description=dj_svg.__doc__,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xshapira/dj-svg",
    author="Max Shapira",
    author_email="max@winoutt.com",
    maintainer="Max Shapira",
    maintainer_email="max@winoutt.com",
    install_requires=["Django>=1.8"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        # "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    test_suite="tests",
)

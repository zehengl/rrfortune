from setuptools import setup, find_packages

from rrfortune import VERSION

with open("requirements-test.txt") as f:
    tests_require = f.readlines()

setup(
    name="rrfortune",
    version=VERSION,
    packages=find_packages(),
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    test_suite="tests",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    description="A RenRen Fortune Collector",
    license="MIT",
    url="https://github.com/zehengl/rrfortune",
)

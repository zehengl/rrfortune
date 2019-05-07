from setuptools import setup, find_packages

from rrfortune import VERSION

setup(
    name="rrfortune",
    version=VERSION,
    packages=find_packages(),
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "rollbar", "selenium", "urllib3==1.24.3"],
    test_suite="tests",
    author="Zeheng Li",
    author_email="imzehengl@gmail.com",
    maintainer="Zeheng Li",
    maintainer_email="imzehengl@gmail.com",
    description="A RenRen Fortune Collector",
    license="MIT",
    url="https://github.com/zehengl/rrfortune",
)


from setuptools import setup, find_packages

setup(
    name='rrfortune',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['selenium'],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'rollbar'
    ],
    test_suite='tests',
    author='Zeheng Li',
    author_email='imzehengl@gmail.com',
    maintainer='Zeheng Li',
    maintainer_email='imzehengl@gmail.com',
    description='A renren fortune collector',
    license='MIT',
    url='https://github.com/zehengl/rrfortune',
)

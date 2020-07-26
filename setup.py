from setuptools import setup

with open('README.md') as f:
    lgd = f.read()

setup(
    name='marno',
    version='0.0.1',
    description='',
    long_description=lgd,
    license='MIT',
    author='Alan Bernstein',
    author_email='alan.bernstein@pm.me',
    packages=[
        'marno',
        'tests'
    ],
    install_requires=[
        'requests',
        'bs4'
    ],
    test_suite='tests'
)

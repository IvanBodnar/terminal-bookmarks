from setuptools import setup, find_packages

setup(
    name='python-template',
    version='0.1',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        run=main:run
    ''',
)

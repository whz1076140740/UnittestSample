try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import hw4_library


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='hw4_library',
    version=hw4_library.__version__,
    description='Example library',
    author='Wu Hangze',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/whz1076140740/PythonHomeWork4.git',
    classifiers=[
        'Programming Language :: Python :: 3.12.0'
    ]
)

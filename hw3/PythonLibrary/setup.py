from setuptools import find_packages, setup

setup(
    name='diabetes_mellitus_library',
    packages=find_packages(),
    version='0.1.0',
    description='Python Library for hmw3',
    author='Mathieu Breier, Edward Monbiot, Oliver Gatland',
    install_requires=['pandas', 'numpy', 'scikit-learn']
)
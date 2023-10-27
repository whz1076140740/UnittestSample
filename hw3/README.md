# Computing for Data Science homework 3
### Team members: Oliver Gatland, Ed Monbiot, Mathieu Breier

## Instructions for library installation
Create a virtual environment with the correct dependencies and use "pip install -e." when in the main library folder. You should then be able to import the functions from within the library.





## Procedure to create a library from scratch
1. Create a environment from terminal 
    conda create --name env python=3.11 (for example)

2. Activate the environment 
    conda activate env

3. Structure the folder in the following way:
    * **main_folder** (PythonLibrary)
        * **Setup.py** file with the following content : 
                    from setuptools import find_packages, setup
                    setup(
                        name='diabetes_mellitus_library',
                        packages=find_packages(),
                        version='0.1.0',
                        description='Python Library for hmw3',
                        author='Mathieu Breier, Edward Monbiot, Oliver Gatland',
                        install_requires=['pandas', 'numpy', 'scikit-learn']
                    )
        - **Folder of the library project** (will include the different sections where we can store the different functions according to their use)
            - **folder1** (ex: Cleaning)
                - **__init__.py** file with the following content!!!:
                    from .CleaningFunctions import *
                - **CleaningFunctions.py** (python text file with the functions included)
            - **folder2** (ex: Training)
                - **__init__.py** file with the following content!!!:
                    from .TrainingFunctions import *
                - **TrainingFunctions.py** (python text file with the functions included)
            - **EMPTY __init__.py** file
        - Optional **README.md file**

4. Move the terminal directory to the main_folder (PythonLibrary)

5. Execute the command in the terminal: pip install -e. 



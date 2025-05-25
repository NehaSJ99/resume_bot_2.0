from setuptools import find_packages,setup
from typing import List

HYFRN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will return list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYFRN_E_DOT in requirements:
            requirements.remove(HYFRN_E_DOT)
    
    return requirements

setup(
    name = 'Resume-GPT',
    version = '0.0.1',
    author = 'NehaSJ',
    author_email='nehajagtap549@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
from typing import List
from setuptools import find_packages,setup


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Cette fonction va retourner la liste des librairies requises
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Badara",
    author_email="diallodouba17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)

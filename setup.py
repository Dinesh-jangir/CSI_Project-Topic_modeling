'''
The setup.py file is an essential part of python packaging 
and disrubuting python projects. Is is used by setuptools 
(or distutials is older python versions) to define the configuration 
of your project ,such as its metadata ,dependencies, and more 
'''


from setuptools import find_packages,setup
from typing import List 

def get_requirements()->List[str]:
    ''''This function returns a list of requirements'''
    
    requirement_lst:List[str]= []    
    try: 
        with open('requirement.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines -e . 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
                    
                    
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_lst


# setup (
#     name = "NETWORKSECURITY",
#     version = "0.0.1",
#     author = "Dinesh jangir",
#     author_email = "dineshjangir887766@gmail.com",
#     packages = find_packages(),
#     install_requires = get_requirements()
# )

print(get_requirements('requirement.txt'))
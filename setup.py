# set up the SRC folder as a local package ( from src.functions import somethig )
from setuptools import find_packages, setup
setup(packages=find_packages()) 
#find_packages(): will look for the constructor file (__init__.py) in every folder. If it finds it, the folder will be considered as a local package
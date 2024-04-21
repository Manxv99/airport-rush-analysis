from setuptools import find_packages, setup

setup(
    name = 'DiamondPricePrediction',
    version='0.0.1',
    author='Manav',
    author_email='manavshah594@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)
from setuptools import setup, find_packages

setup(
    name='analyse_hackathon',
    version='0.3',
    packages=find_packages(exclude=['']),
    license='MIT',
    description='EDSA Analyse Sprint Hackathon',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Francorider/analyse_hackathon.git',
    author='Francois Viljoen',
    author_email='francorider1995@gmail.com'
)

from setuptools import setup, find_packages

setup(
    name='cube',
    version='1.0',
    description='Base API for RaspberryPi cube.',
    url='http://github.com/alcalyn/cube',
    author='Alcalyn',
    author_email='doubjulien@hotmail.fr',
    license='AGPL-3.0',
    packages=find_packages('.'),
    zip_safe=False
)

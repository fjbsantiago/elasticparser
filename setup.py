# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='capmodel',
    version='1.0.0',
    description='Capacity Modelling Tools',
    long_description=long_description,
    url='https://github.com/LibertyGlobal/ComponentsCapacityPlanning',
    author='Liberty Global',
    author_email='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Capacity Modelling Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='capacity modelling',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'elasticsearch>=5.0.0,<6.0.0',
        'suds-jurko==0.6',
        'arrow==0.10.0',
        'pandas==0.20.1',
        'scikit-learn==0.18.1',
    ],
    python_requires='>=3.5',
    extras_require={
        'dev': [],
        'test': ['pytest==3.0.*'],
    },
)
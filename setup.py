import glob
import os

import setuptools

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.rst'), 'r') as f:
    readme = f.read()

setuptools.setup(
    name='rpn_calculator',
    version='1.2.1.3',
    description='RPN calculator for CLI',
    long_description=readme,
    url='https://github.com/massongit/rpn-calculator',
    author='Masaya SUZUKI',
    author_email='suzukimasaya428@gmail.com',
    license='MIT',
    keywords='RPN Calculator',
    packages=setuptools.find_packages(),
    scripts=glob.glob('bin/*'),
    install_requires=[
        'six==1.12.0',
        'zenhan==0.5.2'
    ],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.7'
    ]
)

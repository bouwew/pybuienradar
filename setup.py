# python setup.py --dry-run --verbose install

from distutils.core import setup

setup(
    name='pybuienradar',
    version='0.4', # Should be updated with new versions
    author='Koen Erens',
    author_email='koen.erens@gmail.com',
    py_modules=['pybuienradar'],
    scripts=[],
    data_files=[],
    url='https://github.com/koen01/pybuienradar',
    license='Open Source',
    description='Simple API to access buienradar.nl forecast data from any python3 script.',
    long_description=open('README.md').read()
)

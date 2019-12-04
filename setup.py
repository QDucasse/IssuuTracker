from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import IssuuTracker

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='IssuuTracker',
    description='Coursework2-Industrial Programming',
    # The project's main homepage.
    url='https://github.com/QDucasse/IssuuTracker',
    # Author details
    author='Quentin Ducasse, Eliott Blondin',
    author_email='qd14@hw.ac.uk',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Programming',
        'Topic :: Scientific/Engineering :: Data Science',
        'Topic :: Utilities',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',

        # OS the application was developed on
        'Operating System :: Apple :: OSX'
    ],

    packages=find_packages(),

    install_requires=['matplotlib','graphviz','pytest'],
    entry_points={"console_scripts": ["qducasse=IssuuTracker.__main__:main"]},

)

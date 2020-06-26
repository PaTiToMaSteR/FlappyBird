"""
To Build this package, open this directory in the pipenv shell and run this command:
    >   pip install wheel
    >?  python setup.py clean --all bdist_wheel
    >?  python setup.py build

To upload after building using twine and our pypi server configuration,
again from the pipenv shell, run:
"""

import os
from setuptools import setup, find_packages
import configparser


# Code to Acquire the dependencies from the PipLock file
def get_requirements_from_pipfile():
    pipfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Pipfile')
    config = configparser.ConfigParser()
    config.read(pipfile)
    packages_dict = dict(config["packages"])
    requirements = list()
    for package, version in packages_dict.items():
        version = version[1:-1]
        if version == '*':
            requirements.append(package)
        else:
            requirements.append("{} {}".format(package, version))
    return requirements


# Gather other attributes we care about for building
REQUIREMENTS = get_requirements_from_pipfile()
PACKAGES = find_packages('.', exclude=['*tests*'])
print("Included Packages: {}".format(PACKAGES))
with open('VERSION', 'r') as f:
    VERSION = f.readlines()[0].strip()
with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

from setuptools import setup, find_packages

setup(
    #entry_points={'fython.plugins': ['installFunction = FictionExtensionManager.bootstrap:install']},
    name="FlappyBird",
    version=VERSION,
    author="Fiction Factory - Fython team",
    author_email='kat-devs@king.com',
    license='King Inc.',
    description="The custom version of KAT-HUB embedded in Fiction Editor",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    #url="https://github.int.midasplayer.com/FictionFactory/FictionExtensionKit",
    package_dir={'': '.'},
    packages=PACKAGES,
    package_data={'FlappyBird': ['*.ui', 'resources/*', '__generated__/**']},
    install_requires=REQUIREMENTS,
    include_package_data=False,
    classifiers=[
        "Operating System :: OS Independent",
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Technical-Artists, Developers, Users',
        'Topic :: Software Development :: Extension Manager',
        'License :: OSI Approved :: King Inc.',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.8',
    zip_safe=False
)

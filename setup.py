from setuptools import setup, find_packages
import versioneer

import os
import io

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='atdict',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Attribute-access ordered dictionary',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tai Sakuma',
    author_email='tai.sakuma@gmail.com',
    url='https://github.com/alphatwirl/atdict',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    extras_require={
        'tests': [
            'pytest>=6.2',
            'pytest-cov>=2.11'
        ]
    }
)

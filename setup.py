import os
import sys

from setuptools import setup
from setuptools import find_packages

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
]

tests_requires = [
    'pytest',
    'mock',
    'webtest',
    'pytest-cov',
    'pytest-xdist',
    'pytest-cache',
]

setup(
    name='dfsocial',
    version='0.0',
    description='dfsocial',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='dfsocial',
    install_requires=requires,
    tests_requires=tests_requires,
    cmdclass={'test': PyTest},
    entry_points="""\
    [paste.app_factory]
    main = dfsocial:main
    [console_scripts]
    initialize_dfsocial_db = dfsocial.scripts.initializedb:main
    """
)

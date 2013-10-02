import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid<1.5-dev',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'formalchemy',
    'pyramid_formalchemy',
    'pyramid_fanstatic',
    'fanstatic==0.16',
    'fa.jquery',
    ]

setup(name='pybr9.fajquery_example',
      version='0.0',
      description='pybr9.fajquery_example',
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
      test_suite='pybr9fajquery_example',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pybr9fajquery_example:main
      [console_scripts]
      initialize_pybr9.fajquery_example_db = pybr9fajquery_example.scripts.initializedb:main
      """,
      )

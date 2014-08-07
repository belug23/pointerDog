import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = ['pyramid', 'pyramid_debugtoolbar', 'pymongo', 'uwsgi', 'waitress']

setup(name='pntr_dog',
      version='0.0',
      description='pntr_dog',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Niall O'Higgins",
      author_email='nialljohiggins@gmail.com',
      url='https://github.com/niallo/pyramid_mongodb',
      keywords='web pyramid pylons mongodb',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pntr_dog",
      entry_points = """\
      [paste.app_factory]
      main = pntr_dog:main
      """,
      paster_plugins=['pyramid'],
      )


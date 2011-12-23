from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='tzicatl.themes.noenieto',
      version=version,
      description="Plone theme for noenieto.com",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "License :: Other/Proprietary License", 
        ],
      keywords='plone theme',
      author='Noe Nieto',
      author_email='nnieto@noenieto.com',
      url='http://noenieto.com/',
      license='proprietary',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tzicatl', 'tzicatl.themes'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

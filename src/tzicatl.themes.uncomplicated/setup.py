from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='tzicatl.themes.uncomplicated',
      version=version,
      description="Diazo theme based on a free css template",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone theme diazo blue uncomplicated',
      author='Noe Nieto',
      author_email='tzicatl@gmail.com',
      url='https://github.com/tzicatl/noenieto',
      license='Custom',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tzicatl', 'tzicatl.themes'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.xdv',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      #setup_requires=["PasteScript"],
      #paster_plugins=["ZopeSkel"],
      )

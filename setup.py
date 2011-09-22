from setuptools import setup, find_packages

version = '0.0'

setup(name='TodoList',
      version=version,
      description="A megrok.scaffold showcase application",
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'
        ],
      keywords="",
      author="Danilo G. Botelho",
      author_email="danilogbotelho@yahoo.com",
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'fanstatic',
                        'zope.fanstatic',
                        'grokcore.startup',
                        # Add extra requirements here
                        'megrok.scaffold'
                        ],
      entry_points={
          'fanstatic.libraries': [
              'todolist = todolist.resource:library',
          ]
      })

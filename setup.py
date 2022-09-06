from setuptools import setup
#!/usr/bin/env python3

setup(name='dev_aberto_jonathans',
      version='0.1',
      packages=['dev_aberto'],
      install_requires=[
        'pacote>=1.0',
        'pacote2'
      ],
    scripts=['scripts/hello.py'],
      )
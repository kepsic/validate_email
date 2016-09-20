from setuptools import setup, find_packages

setup(name='validate_email',
      version = '1.3.1',
      download_url = 'git@github.com:kepsic/validate_email.git',
      packages=['validate_email'],
      author = 'Syrus Akbary, Andres Kepler',
      author_email = 'ime@syrusakbary.com,andres@kepler.ee',
      description = 'validate_email verifies if an email address is valid and really exists.',
      long_description=open('README.rst').read(),
      keywords = 'email validation verification mx verify',
      url = 'http://github.com/kepsic/validate_email',
      license = 'LGPL',
      install_requires=[
                'py3DNS',
                      ],
      scripts=['bin/check-email'],

    )

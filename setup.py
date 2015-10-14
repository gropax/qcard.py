from setuptools import setup

setup(name='qcard',
      version='0.0.0',
      description='Generate flashcards from and to different formats',
      url='http://www.github.com/gropax/qcard.py',
      author='gropax',
      author_email='maximedelaudrin@gmail.com',
      license='MIT',
      packages=['qcard'],
      scripts=['bin/qcard'],
      zip_safe=False)

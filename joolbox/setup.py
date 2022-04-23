from setuptools import setup

setup(
    name='joolbox',
    packages=['joolbox'],
    description='Analytics toolkit',
    version='0.1.6',
    url='https://github.com/ShamanJaggia/joolbox',
    author='shaman jaggia',
    author_email='shaman.jaggia@gmail.com',
    keywords=['pip', 'joolbox'],
    install_requires=[
       "numpy",
       "pandas",
       "matplotlib",
       "seaborn",
       "sklearn",
       "scipy",
       "typing"]
    )
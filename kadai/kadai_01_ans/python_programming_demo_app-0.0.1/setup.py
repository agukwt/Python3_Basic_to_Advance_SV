try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name='python_programming_demo_app',
    version='0.0.1',
    packages=['roboter', 'roboter.models', 'roboter.controller', 'roboter.views'],
    # You could use find_packages if setuptools is installed. 
    # packages=find_packages(),
    package_data={ 'roboter': ['templates/*.txt'] },
    url='http://sakaijunsoccer.appspot.com',
    license='MIT',
    author='jsakai',
    author_email='example@example.com',
    # You can specify install_requires if setuptools is installed
    # install_requires=['termcolor==1.1.0'],
    long_description=open('README.txt').read(),
)

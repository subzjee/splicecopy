from setuptools import setup, find_packages

setup(
    name='splicecopy',
    version='0.1',
    license='MIT',
    author="Stan Bergevoet",
    author_email='stanbergevoet@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/subzjee/splicecopy',
    keywords='copy fastcopy linux',
)
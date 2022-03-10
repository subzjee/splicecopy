from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Copy files using `splice` syscall",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    python_requires=">=3.10"
)
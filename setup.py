import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfastq_filter",
    version="0.2.0",
    author='Andy Hauser',
    author_email='Andreas.Hauser@LMU.de',
    license='LICENSE',
    description='filters FASTQ files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ahcm/pyfastq_filter',
    packages=setuptools.find_packages(),
    scripts=['pyfastq_filter.py'],
    entry_points={ 'console_scripts': [ 'pyfastq_filter=pyfastq_filter:main', ], },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


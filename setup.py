from setuptools import setup, find_packages
import os
import glob

requirements = []
with open('requirements.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        requirements.append(line.strip())

packages = find_packages(exclude=['ez_setup', 'tests', 'tests.*'])
print(packages)

 
setup(
    author = 'fsan',
    author_email = "pabyo.sansinaeti@gmail.com",
    url = 'https://github.com/fsan/loadart',
    download_url = 'https://github.com/fsan/loadart/releases/download/0.1.0/loadart-0.1.0.tar.gz',
    name = 'loadart',
    version = '0.1.0',
    packages = packages,
    data_files=[
        ('loadart/tests/res/',list(glob.glob('loadart/tests/res/*.json'))),
    ],
    description = 'A simple module for loading artifacts from http or local and managing them',
    author = '',
    author_email = '',
    keywords = ['artifact management'],
    install_requires=requirements,
    python_requires='>=3.6',
)


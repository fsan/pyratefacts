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
    url = 'https://github.com/fsan/pyratefacts',
    download_url = 'https://github.com/fsan/pyratefacts/releases/download/1.0.0/pyratefacts-1.0.0-py3-none-any.whl',
    name = 'pyratefacts',
    version = '1.0.0',
    packages = packages,
    description = 'A simple module for loading artifacts from http or local and managing them',
    long_description = "A simple module for loading artifacts from http or local and managing them",
    keywords = ['artifact management'],
    install_requires=requirements,
    python_requires='>=3.6',
)


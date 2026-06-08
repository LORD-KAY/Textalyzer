from codecs import open
from os import path

from setuptools import setup

base_dir = path.abspath(path.dirname(__file__))

# Getting the long description from the md file
with open(path.join(base_dir, "README.md"), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='textalyzer',
    packages=['textalyzer'],
    version='0.2.0',
    description='A text analyzer for repeating and contraction characters',
    long_description=str(long_description),
    long_description_content_type='text/markdown',
    author='Lord Kay',
    author_email='offeilord@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/LORD-KAY/Textalyzer',
    download_url='https://github.com/LORD-KAY/Textalyzer/archive/refs/tags/v0.2.0.tar.gz',
    project_urls={
        'Source': 'https://github.com/LORD-KAY/Textalyzer'
    },
    keywords=['python', 'replacers', 'words', 'repeat', 'characters'],
    python_requires='>=3.8',
    install_requires=['nltk>=3']
)

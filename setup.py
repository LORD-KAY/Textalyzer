from setuptools import setup, find_packages
from codecs import open
from os import path

with open(os.path.join(base_dir,"README.md"),encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = 'textalyzer',
	packages = ['textalyzer'],
	version = '0.1.4',
	description = ' A text  analyzer for repeating and contraction characters',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	author = 'Lord Kay',
	author_email = 'offeilord@gmail.com',
	license = 'MIT',
	classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2'
      ],
	url = 'https://github.com/LORD-KAY/Textalyzer',
	download_url = 'https://github.com/LORD-KAY/Textalyzer/releases/v0.1.5',
	keywords = ['python','replacers','words','repeat','characters'],
	)
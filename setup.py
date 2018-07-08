from setuptools import setup, find_packages
from codecs import open
from os import path

base_dir  = path.abspath(path.dirname(__file__))

#Getting the long description from the md file
with open(path.join(base_dir,"README.md"), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = 'textalyzer',
	packages = ['textalyzer'],
	version = '0.1.6',
	description = ' A text  analyzer for repeating and contraction characters',
	long_description = str(long_description),
	author = 'Lord Kay',
	author_email = 'offeilord@gmail.com',
	license = 'MIT',
	classifiers=[
		  'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2'
      ],
	url = 'https://github.com/LORD-KAY/Textalyzer',
	download_url = 'https://github.com/LORD-KAY/Textalyzer/releases/v0.1.5',
	project_urls={
		'Source':'https://github.com/LORD-KAY/Textalyzer'
	},
	keywords = ['python','replacers','words','repeat','characters'],
	install_requires=['wordnet']
	)
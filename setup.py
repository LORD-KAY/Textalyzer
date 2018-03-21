import os
from distutils.core import setup

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir,"README.rst")) as f:
	long_description = f.read()

setup(
	name = 'textalyzer',
	packages = ['textalyzer'],
	version = '0.1.3',
	description = ' A text  analyzer for repeating and contraction characters',
	long_description = long_description,
	author = 'Lord Kay',
	author_email = 'offeilord@gmail.com',
	license = 'MIT',
	classifiers=[
          'Development Status :: v0.1.3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT',
          'Programming Language :: Python :: 3, Python :: 2'
      ],
	url = 'https://github.com/LORD-KAY/Textalyzer',
	download_url = 'https://github.com/LORD-KAY/Textalyzer/releases/v0.1.3',
	keywords = ['python','replacers','words','repeat','characters'],
	)
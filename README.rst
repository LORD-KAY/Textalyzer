# Textalyzer
Textalyzer is a lightweight python module or library to help ease analyzing of text or words in a particular sentence and manipulating it.
Textalyzer analyze repeating words, contracted words or contractions and formatting them properly.

# Class Functions Involved in this module
  [-] RegexpReplacer <br>
  [-] RepeatCharacter

# Usage
  -Place the file in a folder where you have either read or write and read permisson. Eg. /opinionmining/lib/Textalyzer.py<br/>
  -Import the module into your application.<br/>
   <hr/> 
    from opinionmining.lib.Textalyzer import "Function To Use" <br>
    sample = "I can't wait for the football match" <br>
    object = RegexpReplacer() <br>
    data = object.replace(sample)<br>

# Sample
  ## Repeating words
  - Repeating words like helloooooooooooo - textalyzer help format this word by removing the o's to its normal word "hello"<br/>
  - Contractions like I'm - Textalyzer help format this word by converting it to it's normal word "I am"
# PyPI
- Textalyzer is available at python package index.
  ## Installation Guide
    - Download textalyzer using pip<br>
    - pip install textalyzer<br>
    - Import textalyzer into your project by using ```from Textalyzer import RegexpReplacer,RepeatCharacter``` depending on the   function you want to use.<br>
    
  ## Alternatively
    - [x] You can download the tarball file from `pypi.python.org/pypi/textalyzer`
    - [x] Extract the tarball file
    - [x] Navigate into the extracted folder and install using `python setup.py install`
    
  **To Check Whether it's installed**
  - type  `pip freeze` to display the list of installed packages
# Why This
- Textalyzer is mostly used by python programmers who are more involved with Natural Language Processing , Machine Learning, Text Extraction and others.

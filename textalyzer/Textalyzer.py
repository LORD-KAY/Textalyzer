# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 04:19:37 2017

@author: lord
"""

import re
from nltk.corpus import wordnet

replacement_patterns = [
(r'won\'t','will not'),
(r'Won\'t','Will not'),
(r'can\'t','cannot'),
(r'Can\'t','Can not'),
(r'don\'t','do not'),
(r'Don\'t','Do not'),
(r'it\'s','it is'),
(r'It\'s','It is'),
(r'shan\'t','shall not'),
(r'Shan\'t','Shall not'),
(r'i\'m','i am'),
(r'I\'m','I am'),
(r'ain\'t','is not'),
(r'Ain\'t','Is not'),
(r'you\'re','you are'),
(r'You\'re','You are'),
(r'aren\'t','Are not'),
(r'Aren\'t','Are not'),
(r'\\n\\n','\n'),
(r'\\n','\n'),
(r'\'',''),
(r'\\r\n','\n'),
(r'\\r',''),
(r'/',' '),
(r'\[',''),
(r'\{',''),
(r'\}',''),
(r'\]',''),
(r':',''),
(r'data',''),
(r'Anonymous',''),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t','\g<1> not'),
(r'(\w+)\'ve','\g<1> have'),
(r'(\w+)\'s','\g<1> is'),
(r'(\w+)\'re','\g<1> are'),
(r'(\w+)\'r','\g<1> are'),
(r'(\w+)\'d','\g<1> would'),

]

#class for replacing characters
class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
    def replace(self,text):
        s = text
        for (pattern, repl) in self.patterns:
            (s,count) = re.subn(pattern, repl, s)
        return s
        
#Class for removing the repeating characters
class RepeatCharacter(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
    
    def replace(self, word):
        if wordnet.synsets(word):
            return  word
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word

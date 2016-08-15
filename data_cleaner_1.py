#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib
from bs4 import BeautifulSoup
import string
import re
from collections import OrderedDict



html_content = urllib.urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bs4Obj = BeautifulSoup(html_content, "html.parser")
content = bs4Obj.find("div", {"id":"mw-content-text"}).get_text()



def cleaninput(input):
    input = re.sub("\n", " ", input)
    input = re.sub("\[[0-9]*\]", "", input)
    input = re.sub(" +", " ", input)
    clean_input = []
    input = input.split(" ")
    for item in input:
        item = item.strip(string.punctuation)
        if len(item)>1 or (item.lower()== 'a' or item.lower()== 'i'):
            clean_input.append(item)
    return clean_input

def n_grams(input, n):
    input = cleaninput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

ngrams_2 = n_grams(content,2)
# ngrams_2 = OrderedDict(sorted(ngrams_2.items(),key=lambda t: t[1], reverse=True))
print ngrams_2
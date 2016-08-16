#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
from bs4 import BeautifulSoup
import string
import re
from collections import OrderedDict


hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


req = urllib2.Request("https://en.wikipedia.org/wiki/Python_(programming_language)", headers=hdr)
html_content = urllib2.urlopen(req)
bs4Obj = BeautifulSoup(html_content, "html.parser")
content = bs4Obj.find("div", {"id": "mw-content-text"}).get_text()


def cleaninput(input):
    input = re.sub("\n", " ", input)
    input = re.sub("\[[0-9]*\]", "", input)
    input = re.sub(" +", " ", input)
    clean_input = []
    input = input.split(" ")
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_input.append(item)
    return clean_input


def getNgrams(input, n):
    input = cleaninput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output



ngrams_2 = getNgrams(content, 2)
ngrams_2 = OrderedDict(sorted(ngrams_2.items(),key=lambda t: t[1], reverse=True))
print ngrams_2
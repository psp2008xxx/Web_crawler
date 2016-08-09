# from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

html = urllib.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'html.parser')
# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
print(bsObj.find(src = "../img/gifts/img1.jpg").parent.previous_sibling.get_text())
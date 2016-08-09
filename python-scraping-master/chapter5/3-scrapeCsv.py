import csv
import urllib2
from bs4 import BeautifulSoup
import codecs

html = urllib2.urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, 'html.parser')
# The main comparison table is currently the first table on the page
table = bsObj.find_all("table", {"class": "wikitable"})[0]
rows = table.find_all("tr")

csvFile = open("../files/editors.csv", 'w')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow([unicode(s).encode("utf-8") for s in csvRow])
finally:
    csvFile.close()

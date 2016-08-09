import urllib2
import urllib
import re
import os
from bs4 import BeautifulSoup


def reporthook(block_read, block_size, total_size):
    if not block_read:
        print "Connection Open..."
        return
    if total_size < 0:
        print "Read %s blocks or (%s bytes)" % (block_read, block_read * block_size)
    else:
        ammount_read = block_read * block_size
        print "Read %s blocks or %d/%d" % (block_read, ammount_read, total_size)
    return


def jpg_download(url):
    html_content = urllib.urlopen(url)
    bs4Obj = BeautifulSoup(html_content, 'html.parser')
    image_locations = bs4Obj.find_all("img", src=re.compile("jpg$"))
    for link in image_locations:
        urllib.urlretrieve(link.attrs["src"], os.path.join("D:\userdata\kuni\PycharmProjects\web_crawler\image",
                                                           link.attrs["src"].split("/")[-1]), reporthook=reporthook)


jpg_download("http://www.netbian.com")

# html_content = urllib.urlopen("http://www.pythonscraping.com")
# bs4Obj = BeautifulSoup(html_content, 'html.parser')
# down_load_list = bs4Obj.find_all(src=True)
# print down_load_list
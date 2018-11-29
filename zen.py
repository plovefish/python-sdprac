import urllib.request
from bs4 import BeautifulSoup
from random import randint

# fetch the full html
fp = urllib.request.urlopen("https://www.python.org/dev/peps/pep-0020/")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()

# fetch the zen of python
soup = BeautifulSoup(mystr, 'html.parser')
txt = soup.pre.string
list_lines = txt.splitlines()
index_one = randint(1, 19)

print(list_lines[index_one])

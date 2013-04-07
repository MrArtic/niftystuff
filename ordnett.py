from urllib import urlopen
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import sys


argument_list = sys.argv

lang = argument_list[1]
query = argument_list[2]

# query = str(sys.argv)



webpage = urlopen('http://ordnett.no/search?search='+query+'&lang='+lang).read()

resultList = re.compile('<div class="shortform">(.*)</div>')


findStuff = re.findall(resultList,webpage)


len(findStuff)

listIterator = []
listIterator[:] = range(0, len(findStuff))

for i in listIterator:
	print findStuff[i]
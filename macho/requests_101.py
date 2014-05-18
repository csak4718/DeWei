import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


theurl='http://www.gap.com'
r = requests.get(theurl)# Get a webpage, this creates a Response object called "r"
# print r.text
soup = BeautifulSoup(r.text)
divs=soup.find_all('div')
for div in divs:
	print div
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


theurl='http://www.gap.com' 
r = requests.get(theurl)
print r.text
soup = BeautifulSoup(r.text)

#Web scraping is the process of collecting and parsing raw data from the Web
#Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files.

import requests
from bs4 import BeautifulSoup
re=requests.get("https://shirish137.github.io/shirishonline/")

#print(re)
#print(re.content)

s=BeautifulSoup(re.content,'html.parser')
#print(s)

#a=s.find_all('p')
#print(a)
print(a[0].get_text())

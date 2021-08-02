import requests
from bs4 import BeautifulSoup
source = 'https://books.toscrape.com'
URL = requests.get(source).text
soup = BeautifulSoup(URL, 'lxml')
# Loops through all the article tags with the class named product pod
for div_finder in soup.findAll('article', class_='product_pod'):
    name = div_finder.h3.text    # Gets all the books name which are under the h3 tags inside the div.
    print(name)

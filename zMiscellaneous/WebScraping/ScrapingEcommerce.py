import requests
from bs4 import BeautifulSoup

# Getting Value from the First Page
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 0
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    count  = count + 1
    print(str(count) + '. itemPrice: ' +  itemPrice, 'itemName: ' + itemName)



# Getting Value from the All the Pages

pages = soup.find('ul', class_='pagination')

urls = []

links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum is not None:
        x = link.get('href')
        urls.append(x)
print(urls)



print('\nGetting Value from the All the Pages')
count = 0
for i in urls:
    newURL = url + i
    response = requests.get(newURL)

    soup = BeautifulSoup(response.text, 'lxml')

    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        count = count + 1
        print(str(count) + '. itemPrice: ' + itemPrice, 'itemName: ' + itemName)
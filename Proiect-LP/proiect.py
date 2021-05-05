import requests
from bs4 import BeautifulSoup

url = "https://www.primariahunedoara.ro/ro/info-util/urbanism-cu-si-ac"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
html = BeautifulSoup(page.text, 'html.parser')

titlu = html.find_all('h4')
context = html.find_all('p')

for titlu in titlu:
    print(titlu, end="\n"*2)

for context in context:
    print(context, end="\n"*2)
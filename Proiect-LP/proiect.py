import requests
from bs4 import BeautifulSoup

url = "https://www.primariatm.ro/urbanism/certificate-de-urbanism/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("div", class_= 'card-body')

for results in results:
        print(results, end="\n"*2)

for results in results:
        nrSdate = results.find("p", class_="mb-0 card-title")
                #nrSdate = numar si date
        beneficiar = results.find("p", class_="mb-1 card-text")
        adresa = results.find("p", class_="mb-1 card-text")

        if None in (nrSdate, beneficiar, adresa):
                continue

        print(nrSdate)
        print(beneficiar)
        print(adresa)
        print()
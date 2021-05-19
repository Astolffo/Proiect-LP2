import urllib
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://xpage.primariatm.ro/lotusweb.nsf/certificateurbanism.xsp")

NDCU = []
#Nr./Data CU
DII = []
#Date identificare imobil
Beneficiar = []
Adresa = []
Descriere = []

table = soup.find("table",{"class" : "xspDataTable"})
dateCU = dateCUsaved = ""
for record in table.find_all("tr"):
    for data in record.findAll("td"):
        newData = data.text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
        dateCU = dateCU + newData + "\t"
    dateCU = dateCU + "\n"
#print(dateCU)

#file = open("CertificateUrbanismIncercari.csv", "w", encoding='utf8')
#file.write(dateCU)
#file.close()

Date = str(dateCU)

for container in Date:
    dateAdresa = container.find(r'')
    Adresa.append(dateAdresa)



file = open("CUIncercari.csv", "w", encoding='utf8')
file.write(dateCUsaved)
file.close()

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

Date = soup.find_all('tr', attrs={'role':'row'})


for container in Date:
    dateNDCU = container.find_all('span', attrs={'id':"view:_id1:dynamicViewPanel1:0:viewColumn6:_internalViewText"})
    NDCU.append(dateNDCU)

    dateDII = container.find_all('span', attrs={'id':"view:_id1:dynamicViewPanel1:0:viewColumn7:_internalViewText"})
    DII.append(dateDII)

    dateBeneficiar = container.find_all('span', attrs={'id': "view:_id1:dynamicViewPanel1:0:viewColumn8:_internalViewText"})
    Beneficiar.append(dateBeneficiar)

    dateAdresa = container.find_all('span', attrs={'id': "view:_id1:dynamicViewPanel1:0:viewColumn9:_internalViewText"})
    Adresa.append(dateAdresa)

    dateDescriere = container.find_all('span', attrs={'id': "view:_id1:dynamicViewPanel1:0:viewColumn10:_internalViewText"})
    Descriere.append(dateDescriere)

tabel = pd.DataFrame({
    'Nr./Data CU':NDCU,
    'Date identificare imobil':DII,
    'Beneficiar':Beneficiar,
    'Adresa':Adresa,
    'Descriere':Descriere,
})

tabel['Nr./Data CU'] = tabel['Nr./Data CU'].str.extract('(\d+)').astype(str)
tabel['Date identificare imobil'] = tabel['Date identificare imobil'].str.extract('(\d+)').astype(str)
tabel['Beneficiar'] = tabel['Beneficiar'].str.extract('(\d+)').astype(str)
tabel['Adresa'] = tabel['Adresa'].str.extract('(\d+)').astype(str)
tabel['Descriere'] = tabel['Descriere'].str.extract('(\d+)').astype(str)
tabel.to_csv('CUIncerc.csv')

table = soup.find("table",{"class" : "xspDataTable"})
dateCU = dateCUsaved = ""
for record in table.find_all("tr"):
    for data in record.findAll("td"):
        newData = data.text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
        dateCU = dateCU + newData + "\t"
    dateCU = dateCU + "\n"
print(dateCU)



file = open("CertificateUrbanism.csv", "w", encoding='utf8')
file.write(dateCU)
file.close()

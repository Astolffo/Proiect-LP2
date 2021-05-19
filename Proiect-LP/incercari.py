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

with open('CertificateUrbanismIncercari.csv', 'r', encoding='utf8') as tsv:
    Date = [line.strip().split('\t') for line in tsv]


for container in Date:
    dateNDCU = container.re.findilter(r'^(\d+\d+\d+).(\d+.\d+.\d+)')
    NDCU.append(dateNDCU)

    dateDII = container.re.findilter(r'(C.F.|CF| C.F.| CF)(Nr.\d+|Nr. \d+| Nr.\d+| Nr. \d+| nr.\d+| nr. \d+|nr.\d+|nr. \d+|CF.\d+)')
    DII.append(dateDII)

    dateAdresa = container.re.findilter(r'')
    Adresa.append(dateAdresa)

    dateDescriere = container.re.findilter('span', attrs={'id': "view:_id1:dynamicViewPanel1:0:viewColumn10:_internalViewText"})
    Descriere.append(dateDescriere)

tabel = pd.DataFrame({
    'Nr./Data CU':NDCU,
    'Date identificare imobil':DII,
    'Adresa':Adresa,
    'Descriere':Descriere,
})

tabel['Nr./Data CU'] = tabel['Nr./Data CU'].str.extract('(\d+)').astype(str)
tabel['Date identificare imobil'] = tabel['Date identificare imobil'].str.extract('(\d+)').astype(str)
tabel['Adresa'] = tabel['Adresa'].str.extract('(\d+)').astype(str)
tabel['Descriere'] = tabel['Descriere'].str.extract('(\d+)').astype(str)
tabel.to_csv('CUIncerc.csv')

table = soup.find("table",{"class" : "xspDataTable"})
dateCU = dateCUsaved = ""
for record in table.find_all("tr"):
    for data in record.findAll("td"):
        newData = data.text.replace("\t", " ").replace("\n", " ").replace("\r", " ").replace("")
        dateCU = dateCU + newData + "\t"
    dateCU = dateCU + "\n"
print(dateCU)

file = open("CertificateUrbanismIncercari.csv", "w", encoding='utf8')
file.write(dateCU)
file.close()

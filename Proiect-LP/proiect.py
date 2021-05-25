import re
import urllib
import urllib.request
from bs4 import BeautifulSoup


import streamlit as st



def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup("https://xpage.primariatm.ro/lotusweb.nsf/certificateurbanism.xsp")

table = soup.find("table",{"class" : "xspDataTable"})
dateCU = dateCUsaved = ""
for record in table.find_all("tr"):
    for data in record.findAll("td"):
        newData = data.text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
        dateCU = dateCU + newData + "\t"
    dateCU = dateCU + "\n"


file = open("CertificateUrbanismIncercari.csv", "w", encoding='utf8')
file.write(dateCU)
file.close()

Date = str(dateCU)


test_str = Date
regex = r"(\w{3,} nr.\d+|\w{3,}  nr.\d+|\w+ \w{3,} nr.\d+ ap.\d+|\w{3,} \w+\t nr,\d+ bl.- sc.-et.- ap.\d+|\w+ nr.\d\w|\w{3,} nr.\d+ ap.\d+| \w+ \w+ nr.\d+ ap.\d+)"
dateAdresa = re.finditer(regex,test_str)

for nrCautari, adresaGasita in enumerate(dateAdresa,start = 1):
    #print("S-au gasit {nrCautari} ,acestea fiind : {adresaGasita}".format(nrCautari=nrCautari,adresaGasita=adresaGasita.group()))

    locatie = str(adresaGasita.group())

    file1 = open("adrese.txt","w",encoding='utf8')
    file1.write(locatie)
    citire = open("adrese.txt","r",encoding='utf8')
    print(citire)

#st.image("geocoding.jpg")
#st.title("Geocoding Application in Python")

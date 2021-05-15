import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv
import pandas as pd

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
print(dateCU)

file = open("CertificateUrbanism.tsv", "w", encoding='utf8')
file.write(dateCU)
file.close()
#are diacritice si apare unicode

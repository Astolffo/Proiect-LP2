import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

dateCU = dateCUsaved =  ""
soup = make_soup("https://xpage.primariatm.ro/lotusweb.nsf/certificateurbanism.xsp")
for record in soup.findAll('tr'):
    for data in record.findAll('td'):
        dateCU = dateCU + ", " + data.text
    if len(dateCU) != 0:
        dateCUsaved = dateCUsaved + "\n" + dateCU[1:]
print(dateCUsaved)

header = "Nr./Data CU, Data identificare, Beneficiar, Adresa, Descriere"
file = open(os.path.expanduser("CertificateUrbanism.csv"),"wb")
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(dateCUsaved, encoding="ascii", errors='ignore'))
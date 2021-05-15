import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

textIntrare = "abcd"
print(textIntrare)
textIesire = textIntrare.replace("b", "")
print(textIesire)

file = open("textIncercari.tsv", "w")
file.write(textIesire)
file.close()
"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")
except urllib.error.URLError:
    print("Deu erro")
else:
    print("Deu certo")
import re
from bs4 import BeautifulSoup
import requests
from libs.headers import headers

def get_valor_moeda(moeda):
    url = f"https://www.google.com/search?q={moeda}+hoje"
    site = requests.get(url, headers=headers)
    if site.status_code != 200:
        return {"error": "Request with status code " + site.status_code}
    soup = BeautifulSoup(site.content, 'html.parser')
    results = soup.find('span', class_="DFlfde SwHCTb").get_text().strip()
    return {"valor": results,
            "moeda": moeda}
    
def get_valor_criptomoeda(moeda):
    url = f"https://www.google.com/search?q={moeda}+hoje"
    site = requests.get(url, headers=headers)
    if site.status_code != 200:
        return {"error": "Request with status code " + site.status_code}
    soup = BeautifulSoup(site.content, 'html.parser')
    results = soup.find('span', class_="pclqee").get_text().strip()
    return {"valor": results,
            "criptomoeda": moeda}
    

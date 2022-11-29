import json

import re
from bs4 import BeautifulSoup
import requests
from libs.headers import headers


def is_not_none(data):
    if data is not None:
        return data.get_text().strip()
    return ""


def get_maiores(tipo):
    url = f"https://site.tc.com.br/analise-investimentos/{tipo}-b3/"

    site = requests.get(url, headers=headers)
    if site.status_code != 200:
        return {"error": "Request with status code " + site.status_code}
    soup = BeautifulSoup(site.content, 'html.parser')
    results = soup.find_all('li', class_="company-list-fullstyles__Row-sc-1pvwj55-1 beCjBk")
    results = results[1:]

    dic_acoes = []
    for result in results:
        indice = result.find('span', class_=re.compile("info-companystyles__Number")).get_text().strip()
        tag = result.find('h2', class_=re.compile("info-companystyles__Ticker")).get_text().strip()
        nome = result.find('span', class_=re.compile("info-companystyles__Name")).get_text().strip()
        variacao = result.find('div', class_=re.compile("company-list-fullstyles__Badge")).get_text().strip()
        dic_acoes.append({"indice": indice, "tag": tag, "nome": nome, "variacao":variacao})
    return dic_acoes

def get_mais(tipo):
    url = f"https://site.tc.com.br/analise-investimentos/{tipo}-b3/"

    site = requests.get(url, headers=headers)
    if site.status_code != 200:
        return {"error": "Request with status code " + site.status_code}
    soup = BeautifulSoup(site.content, 'html.parser')
    results = soup.find_all('li', class_="company-list-fullstyles__Row-sc-1pvwj55-1 beCjBk")
    results = results[1:]

    dic_acoes = []
    for result in results:
        indice = result.find('span', class_=re.compile("info-companystyles__Number")).get_text().strip()
        tag = result.find('h2', class_=re.compile("info-companystyles__Ticker")).get_text().strip()
        nome = result.find('span', class_=re.compile("info-companystyles__Name")).get_text().strip()
        valor = result.find('span', class_=re.compile("company-list-fullstyles__Value-")).get_text().strip()
        dic_acoes.append({"indice": indice, "tag": tag, "nome": nome, "Total termado":valor})
    return dic_acoes

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
from HtmlGenerator import HtmlGenerator

# Classes to reference html divs
STATS_CLASS = "stats"

def get_htmlcode(url):
    r = requests.get("http://" + url)
    data = r.text
    return data


def extract_info(html_code, tag, m_class):
    soup = BeautifulSoup(html_code, "html.parser")
    info = soup.find("table","estadisticas")
    return info


def main():
    pokemon = raw_input("Introdueix un pokemon: ")
    generator = HtmlGenerator(pokemon)
    data = get_htmlcode("es.pokemon.wikia.com/wiki/" + pokemon)
    table = extract_info(data, "table", "estadisticas")
    generator.add_html_code(STATS_CLASS,str(table))
    generator.create_html_file(pokemon)


if __name__ ==  "__main__":
    main()

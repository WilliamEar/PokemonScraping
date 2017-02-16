# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
from HtmlGenerator import HtmlGenerator

# Classes to reference html divs
STATS_CLASS = "stats"
PORTTRAIT_CLASS = ""
def get_htmlcode(url):
    r = requests.get("http://" + url)
    data = r.text
    return data


def create_soup(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    return soup


def main():
    pokemon = raw_input("Introdueix un pokemon: ")

    generator = HtmlGenerator(pokemon)

    data = get_htmlcode("es.pokemon.wikia.com/wiki/" + pokemon)
    soup = create_soup(data)

    table = soup.find("table", class_="estadisticas")

    # from all image select the one which is the pokemon sprite
    all_images = soup.find_all("img")
    for i in all_images:
        if pokemon+".png" in str(i):
            #Store the src of image
            image_src = i["data-src"]
            break

    generator.add_html_header(pokemon, str(image_src))
    generator.add_html_code(STATS_CLASS,str(table))

    generator.create_html_file(pokemon)


if __name__ ==  "__main__":
    main()

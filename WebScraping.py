# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
from HtmlGenerator import HtmlGenerator
from PokemonShelve import PokemonShelve

# Classes to reference html divs
STATS_CLASS = "stats"

def get_htmlcode(url):
    r = requests.get("http://" + url)
    data = r.text
    return data


def create_soup(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    return soup

def beautiful_string(str):
    str = str[0].upper() + str[1:].lower()
    return str

def scrap_stats(soup, data):
    return soup.find("table", class_="estadisticas")


def scrap_header_image(soup, data, pokemon):
    # from all image select the one which is the pokemon sprite
    all_images = soup.find_all("img")
    for i in all_images:
        if pokemon.lower() + ".png" in str(i).lower():
            #Store the src of image
            return i["data-src"]

    return None

def scrap_pokemon_id(soup, data, pokemon):
    pokemon_id = soup.find("span", {'id':'numeronacional'})
    return int(pokemon_id.string)


def main():
    name_database = PokemonShelve("Pokemon_names.db")

    pokemon = raw_input("Introdueix un pokemon: ")
    pokemon.lower().replace(" ","_")

    data = get_htmlcode("es.pokemon.wikia.com/wiki/" + pokemon)
    soup = create_soup(data)

    if not name_database.pokemon_exists(pokemon.replace("_"," ")):
        print "The pokemon you are looking for doesn't exist.\nCheck your spelling."
        exit(1)

    pokemon_id = scrap_pokemon_id(soup, data, pokemon)
    image_src = scrap_header_image(soup, data, pokemon)
    stats = scrap_stats(soup, data)

    pokemon = beautiful_string(pokemon)

    generator = HtmlGenerator(pokemon, pokemon)

    generator.add_html_header(pokemon, str(image_src))
    generator.add_html_code("%s Stats"%(pokemon), STATS_CLASS,str(stats))

    generator.create_html_file()
    generator.open_html_file()

    name_database.end()
    exit(0)

if __name__ ==  "__main__":
    main()

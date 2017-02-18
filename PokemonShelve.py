# -*- coding: utf-8 -*-
import shelve
import os
import requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PokemonShelve:

    __database = None

    def __init__(self, db_path):
        try:
            self.__database = shelve.open(db_path)

            # Saving pokemons' names on db
            if not os.path.exists(db_path):
                self.__save_pokemon()

        except IOError:
            print "Error creating %s database"%(db_path)

    # Close the db
    # Has to be called at the end of program
    def end(self):
        try:
            self.__database.close()
        except IOError:
            print "Error saving changes on database."


    # Returns True if pokemon exists
    def pokemon_exists(self, pokemon_name):
        pokemon_name = pokemon_name.lower()
        return pokemon_name in self.__database.values()

    def __save_pokemon(self):
        r = requests.get("http://es.pokemon.wikia.com/wiki/Lista_de_Pok%C3%A9mon")
        data = r.text
        soup = BeautifulSoup(data, "html.parser")

        # Get all tables
        tables = soup.find_all("table")
        # init the pokemon id
        i = 0
        for current_table in tables:
            if not "radius10" in str(current_table) and not "plegable" in str(current_table):   # Tables with this classes are useless
                table = current_table.find_all("tr")    # Get all table rows
                for row in table[1:]:   # [1:] to skip the table header
                    name = row.find("a")    # The pokemon name is surrounded by an a tag
                    self.__database[str(i)] = name.string.encode("utf-8").lower()
                    i += 1

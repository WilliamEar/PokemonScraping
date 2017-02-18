# -*- coding: utf-8 -*-
import webbrowser
import os

class HtmlGenerator:
    __html_head = ""
    __html_body = ""
    __html_closer = ""'''
                <footer>
                    <p>This is a fanmade app.</p>
                    <p>Made by Guillem Orellana Trullos 2017.</p>
                    <p>
                        Info scraped from <a href="http://es.pokemon.wikia.com/wiki/">WikiDex, la enciclopedia Pokemon</a>
                    </p>
                </footer>
            </div>
        </BODY>
    </HTML>'''

    __file_path = ""

    def __init__(self, title, name):
        self.__file_path = "CreatedWp/" + name + ".html"
        self.__html_head = '''
        <HTML>
            <HEAD>
                <link rel="stylesheet" href="css\style.css">
                <link rel="stylesheet" href="css\stats.css">
                <link rel="stylesheet" href="css\header.css">
                <link rel="stylesheet" href="css\\footer.css">
                <link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet">
                <meta charset="UTF-8">
                <TITLE>%s Stats</TITLE>
            </HEAD>

            <BODY>
                <div class="wrap">'''%(title)


    def add_html_header(self, title, image_src):
        self.__html_body += '''
        <header class="main_title">
            <div class="title"><h1>%s</h1></div>
            <img src="%s">
        </header>'''%(title, image_src)


    def add_html_code(self, name, title, new_html):
        # Adding a new div class to html code
        self.__html_body += '''
        <div class=\"%s added">
            <h1>%s</h1>
            %s
        </div>
        '''%(title, name, new_html)


    def create_html_file(self):
        try:
            final_code = self.__html_head + self.__html_body + self.__html_closer
            f = open(self.__file_path, "w")
            f.write(final_code)
            f.close()
        except IOError:
            print "Error creating/writing the html file."

        return

    def open_html_file(self):
        webbrowser.open_new(os.path.abspath(self.__file_path))

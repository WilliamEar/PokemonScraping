# -*- coding: utf-8 -*-
class HtmlGenerator:
    __html_head = ""
    __html_body = ""
    __html_closer = '''
            </div>
        </BODY>
    </HTML>'''


    def __init__(self, title):
        self.__html_head = '''
        <HTML>
            <HEAD>
                <link rel="stylesheet" href="css\style.css">
                <link rel="stylesheet" href="css\stats.css">
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


    def add_html_code(self, name, new_html):
        # Adding a new div class to html code
        self.__html_body += "<div class=\"%s\">%s</div>"%(name, new_html)


    def create_html_file(self, name):
        path = "CreatedWp/" + name + ".html"
        try:
            final_code = self.__html_head + self.__html_body + self.__html_closer
            f = open(path, "w")
            f.write(final_code)
            f.close()
        except IOError:
            print "Error creating/writing the html file."

        return

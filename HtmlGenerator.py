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
                <link rel="stylesheet" href="style.css">
                <meta charset="UTF-8">
                <TITLE>%s Stats</TITLE>
            </HEAD>

            <BODY>
                <div class="wrap">'''%(title)


    def add_html_code(self, name, new_html):
        self.__html_body += "<div class=\"%s\">%s</div>"%(name, new_html)


    def create_html_file(self, name):
        path = "CreatedWp/" + name + ".html"
        try:
            f = open(path, "w")
            f.write(self.__html_head)
            f.write(self.__html_body)
            f.write(self.__html_closer)
            f.close()
        except IOError:
            print "Error creating/writing the html file."

        return

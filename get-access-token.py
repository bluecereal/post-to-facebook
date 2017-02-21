from urllib2 import urlopen #opens webpage
from HTMLParser import HTMLParser



#define a parser for the html we'll read later
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr

    def handle_endtag(self, tag):
        return tag

    def handle_data(self, data):
        print data
        return data
    
    def handle_comment(self, comment):
        return comment

#get response from server
response = urlopen('http://localhost/login.html')

#read the data 
html = response.read()

#instantiate the parser and feed it html
parser = MyHTMLParser()
parser.feed(html)

#using selenium might be a better idea?

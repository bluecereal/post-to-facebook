from urllib2 import urlopen #opens webpage
from HTMLParser import HTMLParser



#define a parser for the html we'll read later
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    
    def read(self, data):
        self._lines = []
        self.reset()
        self.feed(data)
        return self._lines
    def handle_starttag(self, tag, attrs):
        print "Encountered start tag: ", tag
        if tag == "div":
            print "PORTANT TAG"
        for a in attrs:
            if a == "placeholder":
                print "IMPORTANT PLACEHOLDER", a

    def handle_endtag(self, tag):
        return tag

    def handle_data(self, data):
        return data
        #print "Encountered data!: ", data

    def handle_comment(self, comment):
        return comment

#get response from server
response = urlopen('https://developers.facebook.com/tools/explorer')

#read the data 
html = response.read()

#instantiate the parser and feed it html
parser = MyHTMLParser()
parser.feed(html)


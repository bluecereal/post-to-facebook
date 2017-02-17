from urllib2 import urlopen #opens webpage
from HTMLParser import HTMLParser



#define a parser for the html we'll read later
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    
    def read(self, data):
        self.script_data = []
        self.reset()
        self.feed(data)
        return self.script_data
    
    def handle_starttag(self, tag, attrs):
        return tag

    def handle_endtag(self, tag):
        return tag

    def handle_data(self, data):
        if 'accessToken' in data:
            print "found it!"
            self.script_data.append(data)
        return data

    def handle_comment(self, comment):
        if 'accessToken' in comment:
            print "found it!"
            self.script_data.append(data)
        return comment

#get response from server
response = urlopen('https://developers.facebook.com/tools/explorer')

#read the data 
html = response.read()

#instantiate the parser and feed it html
parser = MyHTMLParser()

#read returns all data within a <script> tag
data = parser.read(html)
#print data
#{"accessToken":null,

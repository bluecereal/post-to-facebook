from urllib2 import urlopen #opens webpage
from HTMLParser import HTMLParser



#define a parser for the html we'll read later
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    
    def read(self, data):
        self.is_script = False
        self.script_data = []
        self.reset()
        self.feed(data)
        return self.script_data
    
    def handle_starttag(self, tag, attrs):
        #print "Encountered start tag: ", tag
        if tag == "script":
            self.is_script = True
            print "script@p", self.getpos() 
            for attr in attrs:
                print "  attr: ", attr
        for a in attrs:
            if a == "placeholder":
                print "IMPORTANT PLACEHOLDER", a

    def handle_endtag(self, tag):
        if tag == "script":
            #print "script block ended"
            self.is_script = False
        return tag

    def handle_data(self, data):
        if self.is_script:
            self.script_data.append(data)
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

#read returns all data within a <script> tag
data = parser.read(html)


import HTMLParser
import urllib

urlText = []

class ParseText(HTMLParser.HTMLParser):
    
    def handle_data(self,data):
        if data != '\n':
            urlText.append(data)
            
#object of class
lparser = ParseText()

thisurl = "http://sthurlow.com/python/lesson06/"

lparser.feed(urllib.urlopen(thisurl).read())

lparser.close()
f = open("ParsedHTML",'w')

for item in urlText:
    f.write(str(item))
    
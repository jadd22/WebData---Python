import urllib

myurl = "http://www-rohan.sdsu.edu/~gawron/index.html"

handle = urllib.urlopen(myurl)

html_gunk = handle.read()

#print(html_gunk)
f = open("myfile",'w')
f.write(str(html_gunk))



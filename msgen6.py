#8.15.21, 9.16.21, and 9.20.22
def dateformat(unixtime):
    timestamp = datetime.datetime.fromtimestamp(unixtime)
    fdate = timestamp.strftime("%B %#d, %Y %#I:%M %p")
    return fdate
def WriteNewLine():
    f.write("\r\n")
import os
import datetime
import glob
search_dir = "notes/"
# remove anything from the list that is not a file (directories, symlinks)
# thanks to J.F. Sebastion for pointing out that the requirement was a list 
# of files (presumably not including directories)
#https://stackoverflow.com/questions/168409/how-do-you-get-a-directory-listing-sorted-by-creation-date-in-python
notes = list(filter(os.path.isfile, glob.glob(search_dir + "*")))
notes.sort(key=lambda x: os.path.getmtime(x))
names = []
dates = []
times = []
sizes = []
isodates = []
html = ""
filename = datetime.datetime.now()
filename = filename.strftime("%Y%m%d%H%M")
filename = "ms " + filename + ".txt"
f = open(filename, "w", encoding="utf-8")
for x in range (0, len(notes)):
    if notes[x].endswith(".txt"):
        title = (notes[x]) #title
        title = title.replace(".txt","")
        title = title.split("\\")
        title = title[1]
        title = "$$$TITLE$$$"+title+"$$$TITLE$$$"
        f.write(title)
        WriteNewLine()
        utime = os.path.getmtime(notes[x])
        ts = dateformat(utime)
        ts = "$$$DATE$$$"+ts+"$$$DATE$$$"
        f.write(ts)
        WriteNewLine()
        testnote = open(notes[x], "rb") #i don't know if the encoding is that tho?
        testnote = testnote.read()
        if testnote[0:2] == b'\xff\xfe':
            curnote = open(notes[x], "r", encoding="utf-16")
            curnote = curnote.read() 
            curnote.encode("utf-8")        
            f.write(curnote)
        else:
            curnote = open(notes[x], "r", encoding="cp1252")
            curnote = curnote.read()
            curnote.encode("utf-8")
            f.write(curnote)
        WriteNewLine()
        WriteNewLine()
f.close()

    
    

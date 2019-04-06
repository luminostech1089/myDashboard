import os
import re
baseDir = os.path.dirname(__file__)
templatesDir = os.path.join(baseDir, 'templates')

htmlFiles = [tFile for tFile in os.listdir(templatesDir) if tFile.endswith('.html')]

hrefPat = 'href="(.*?\.css)"'
jsPat = 'src="(.*?\.js)"'
for htmlfile in htmlFiles:
    newFile = os.path.join(templatesDir, htmlfile+".t")
    nfh = open(newFile, "w+")
    print "Processing file {}".format(htmlfile)
    with open(os.path.join(templatesDir, htmlfile)) as fh:
        for line in fh:
            href = re.search(hrefPat, line)
            js = re.search(jsPat, line)
            if href:
                newline = line.replace(href.group(1), '{{{{url_for(\'static\', filename=\'{css}\')}}}}'.format(css=href.group(1)))
                nfh.write(newline)
            elif js:
                newline = line.replace(js.group(1), '{{{{url_for(\'static\', filename=\'{js}\')}}}}'.format(js=js.group(1)))
                nfh.write(newline)
            else:
                nfh.write(line)
    nfh.close()

for file in os.listdir(templatesDir):
    if file.endswith('.html'):
        print "renaming file {}".format(file)
        fullpath = os.path.join(templatesDir, file)
        os.rename(fullpath, fullpath+".bkp")
        os.rename(fullpath+".t", fullpath.replace(".t", ""))



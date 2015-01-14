from sys import argv

script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
files_text = txt.read()
print files_text
print "now parsing it...."
stuff = files_text.split(',')
for words in stuff:
	print words

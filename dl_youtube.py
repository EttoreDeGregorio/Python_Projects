#!usr/bin/env python

import pafy

url = raw_input("URL = ")
video = pafy.new(url)

print "\nTitle:\t\t",video.title

best = video.getbest(preftype = "mp4")
print "Resolution:\t", best.resolution
print "Format:\t\t", best.extension

print "\n--- PROGRESS ---"
best.download(quiet = False, filepath = "/Users/ettore/Downloads")

print "\n\n----- DOWNLOAD COMPLETED -----"
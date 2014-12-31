# Creates a set of 

import mechanize as mech
import re
import pickle

url = 'https://en.wikipedia.org/wiki/List_of_alternative_rock_artists'

browser = mech.Browser()
browser.set_handle_robots(False)

response = browser.open(url)
print 'Assembling set from {0}'.format(browser.title())

artists = set()

for link in browser.links(url_regex='/wiki/(\+|!|.|\?)*[A-Za-z0-9]+'):
	artist = link.text
	if '[IMG]' not in artist:
		artists.add(artist)


pickle.dump(artists, open('artists.p', 'wb'))

def return_set():
	return artists

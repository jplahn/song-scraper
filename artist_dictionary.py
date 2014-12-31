'''
 Creates a set of artists listd in Wikipedia's alternative rock. Will expand
 include other genres eventually.

 Uses the Mechanize library to access artist names via links and puts them into 
 a set which is then pickled for later use. 

 TODO: adding some "artists" that are actually unrelated links, which isn't a 
 huge deal in the scheme of things since it's veyr little additional storage, but
 it may be nice to clean it up. 
 May also be useful to parse other sites to find any missed artists since checking
 for duplicates is cheap. 

 Jordan Plahn
''' 

import mechanize as mech
import pickle

url = 'https://en.wikipedia.org/wiki/List_of_alternative_rock_artists'

browser = mech.Browser()
browser.set_handle_robots(False)
response = browser.open(url)

print 'Assembling set from {0}'.format(browser.title())

# create new set holding all of the artists
artists = set()


# grab all of the links on the page, matching only those in the form /wiki/artist
for link in browser.links(url_regex='/wiki/(\+|!|.|\?)*[A-Za-z0-9]+'):
	artist = link.text
	# some random cases with [IMG] being parsed
	if '[IMG]' not in artist:
		artists.add(artist)


# produce a pickle to access set in another script
pickle.dump(artists, open('artists.p', 'wb'))

# returns the set in case I prefer to use that instead of accessing the pickle
def return_set():
	return artists

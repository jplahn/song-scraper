import mechanize as mech
import pickle
import re

yUrl = 'https://youtube.com'
mUrl = 'http://www.youtube-mp3.org/'

# browser for YouTube
yBrowser = mech.Browser()
yBrowser.set_handle_robots(False)

yResponse = yBrowser.open(yUrl)
print 'Opening {0}...'.format(yBrowser.title())

# browser for mp3 downloader
mBrowser = mech.Browser()
mBrowser.set_handle_robots(False)

mResponse = mBrowser.open(mUrl)
print 'Opening {0}...'.format(mBrowser.title())


yForm = yBrowser.select_form(nr = 1)
yBrowser['search_query'] = 'city and colour'
yBrowser.submit()

print yBrowser.title()

count = 0
for link in yBrowser.links(url_regex='/watch\?v=[A-Za-z0-9]+'):
	if count < 1:
		address = re.search('/watch\?v=[A-Za-z0-9]+', str(link))
		songUrl = 'https://www.youtube.com' + address.group(0)
		print 'Url of video is {0}'.format(songUrl)
		mForm = mBrowser.select_form(nr = 0)
		mBrowser.set_value(songUrl, nr = 0)
		mBrowser.submit()
		count += 1
	else:
		break

# artists = pickle.load(open('artists.p', 'rb'))


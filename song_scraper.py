import mechanize as mech
import pickle

url = 'https://youtube.com'

br = mech.Browser()
br.set_handle_robots(False)

response = br.open(url)
print br.title()

form = br.select_form(nr = 1)
br['search_query'] = 'city and colour'
br.submit()

print br.title()

artists = pickle.load(open('artists.p', 'rb'))
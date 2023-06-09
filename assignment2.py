import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

html = urllib.request.urlopen(
    'http://py4e-data.dr-chuck.net/known_by_Denis.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags_lst = list()
for x in range(0, count):
    tags = soup('a')
    my_tags = tags[position-1]
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(my_tags.get('href', None))

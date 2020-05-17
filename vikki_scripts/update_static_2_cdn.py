from bs4 import BeautifulSoup
from os.path import basename, splitext
import re

source_file = "C:\\vikki\\github\\tools\\templates\\general.html"
destination_file = "C:\\vikki\\github\\tools\\templates\\general_test.html"

soup = BeautifulSoup(open(source_file), "html.parser")
#match = soup.findAll("script")
#print(match)

for script in soup.findAll('script'):
    print("checking for {}".format(script))
    append = re.findall(r"'(.*?)'", str(script))
    print(append)
    script['src'] = 'https://cdn.jsdelivr.net/gh/vignesh88/cdn/django/tools/' + append[0]
    print(script['src'])
print(str(soup))
#my_html_string = str(soup)
file_obj = open(destination_file, "w+")
file_obj.write(str(soup))
file_obj.close()
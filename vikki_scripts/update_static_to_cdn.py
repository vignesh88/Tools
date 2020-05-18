from bs4 import BeautifulSoup
import re

source_files = ['base', 'base64', 'epoch', 'general', 'geoip', 'home', 'password_generator']
#source_files = ['base-cdn', 'base64-cdn', 'epoch-cdn', 'general-cdn', 'geoip-cdn', 'home-cdn', 'password_generator-cdn']
source_folder = "C:\\vikki\\github\\tools\\templates\\"
destination_folder = "C:\\vikki\\github\\tools\\templates\\"
cdn_base_url = "https://cdn.jsdelivr.net/gh/vignesh88/cdn/django/tools/"
static_base_url_1 = "{% static '"
static_base_url_2 = "' %}"

def update_script_to_cdn(files):
	source = source_folder + files + ".html"
	#destination = destination_folder + files + "-cdn" + ".html"
	soup = BeautifulSoup(open(source), "html.parser")
	for script in soup.findAll('script',{"src":True}):
		print("Parsing TAG {}".format(script))            
		str_append = re.findall(r"'(.*?)'", str(script))
		if str_append:
			current_value = script['src']
			script['src'] = cdn_base_url + str_append[0]
			print("Static URL {0} will be replaced by {1}".format(current_value, script['src']))
	file_obj = open(source, "w+")
	file_obj.write(str(soup))
	file_obj.close()

def update_link_to_cdn(files):
	source = source_folder + files + ".html"
	#destination = destination_folder + files + "-cdn" + ".html"
	soup = BeautifulSoup(open(source), "html.parser")
	for link in soup.findAll('link',{"href":True}):
		print("Parsing TAG {}".format(link))            
		str_append = re.findall(r"'(.*?)'", str(link))
		if str_append:
			current_value = link['href']
			link['href'] = cdn_base_url + str_append[0]
			print("Static URL {0} will be replaced by {1}".format(current_value, link['href']))
	file_obj = open(source, "w+")
	file_obj.write(str(soup))
	file_obj.close()

def update_script_to_static(files):	
	source = source_folder + files + ".html"
	#destination = destination_folder + files.replace("-cdn", "") + "-static" + ".html"
	soup = BeautifulSoup(open(source), "html.parser")
	for script in soup.findAll('script',{"src":True}):
		print("Parsing TAG {}".format(script))            
		str_append = re.findall(r'"(.*?)"', str(script))
		if str_append[0]:
			current_value = script['src']
			script['src'] = static_base_url_1 + str_append[0].split("https://cdn.jsdelivr.net/gh/vignesh88/cdn/django/tools/")[1] + static_base_url_2
			print("CDN URL {0} will be replaced by {1}".format(current_value, script['src']))
	file_obj = open(source, "w+")
	file_obj.write(str(soup))
	file_obj.close()

def update_link_to_static(files):	
	source = source_folder + files + ".html"
	#destination = destination_folder + files.replace("-cdn", "") + "-static" + ".html"
	soup = BeautifulSoup(open(source), "html.parser")
	for link in soup.findAll('link',{"href":True}):
		print("Parsing TAG {}".format(link))            
		str_append = re.findall(r'"(.*?)"', str(link))
		if str_append[0]:
			current_value = link['href']
			link['href'] = static_base_url_1 + str_append[0].split("https://cdn.jsdelivr.net/gh/vignesh88/cdn/django/tools/")[1] + static_base_url_2
			print("CDN URL {0} will be replaced by {1}".format(current_value, link['href']))
	file_obj = open(source, "w+")
	file_obj.write(str(soup))
	file_obj.close()


for files in source_files:
	print("Parsing HTML {}.html ...".format(files))
	#update_script_to_cdn(files)
	#update_link_to_cdn(files)
	update_script_to_static(files)
	update_link_to_static(files)
	
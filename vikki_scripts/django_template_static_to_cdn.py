#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Vignesh Ragupathy
# Website https://www.vikki.in
# Created Date: Fri June 18 17:00:00 GMT+5.30 2020
'''
This script has been build for updating the Staic content to CDN.
'''

# Generic
import sys
import os
from optparse import OptionParser

# Secific
from bs4 import BeautifulSoup
import re

# Variables
cdn_base_url = "https://unpkg.com/vikki-tools@1.0.8/dist/"
static_base_url_1 = "{% static '"
static_base_url_2 = "' %}"

def main():
	usage = "usage: %prog [options] arg"
	target_choices = ['static', 'cdn']
	parser = OptionParser(usage=usage, description="Static to CDN converter")
	parser.add_option('-t', '--target', dest='target', action="store",
	                  choices=target_choices, help="Conversion target: 'static' or 'cdn'")
	parser.add_option('-f', '--files', dest='files',
	                  action='store', help="List of files to convert")
	parser.add_option('-p', '--path', dest='source_path',
	                  help="Path of html files")
	(options, args) = parser.parse_args()

	if options.target is None:
		parser.print_help()
		sys.exit(2)
	elif options.source_path is None and options.files is None:
		options.files = [file for file in os.listdir(
			options.source_path) if "html" in file]

	elif options.files is None:
		options.files = [os.path.join(options.source_path, file) for file in os.listdir(
			options.source_path) if "html" in file]

	else:
		options.files = options.files.split()

	def update_script_to_cdn(files):
		source = files
		soup = BeautifulSoup(open(source), "html.parser")
		for script in soup.findAll('script', {"src": True}):
			print()
			print("Parsing TAG {}".format(script))
			str_append = re.findall(r"'(.*?)'", str(script))
			if str_append:
				current_value = script['src']
				script['src'] = cdn_base_url + str_append[0]
				print("Static URL {0} will be replaced by {1}".format(
					current_value, script['src']))
		file_obj = open(source, "w+")
		file_obj.write(str(soup))
		file_obj.close()

	def update_link_to_cdn(files):
		source = files
		soup = BeautifulSoup(open(source), "html.parser")
		for link in soup.findAll('link', {"href": True}):
			print()
			print("Parsing TAG {}".format(link))
			str_append = re.findall(r"'(.*?)'", str(link))
			if str_append:
				current_value = link['href']
				link['href'] = cdn_base_url + str_append[0]
				print("Static URL {0} will be replaced by {1}".format(
					current_value, link['href']))
		file_obj = open(source, "w+")
		file_obj.write(str(soup))
		file_obj.close()

	def update_script_to_static(files):
		source = files
		soup = BeautifulSoup(open(source), "html.parser")
		for script in soup.findAll('script', {"src": True}):
			print()
			print("Parsing TAG {}".format(script))
			str_append = re.findall(r'"(.*?)"', str(script))
			if str_append[0]:
				current_value = script['src']
				script['src'] = static_base_url_1 + \
					str_append[0].split(cdn_base_url)[1] + static_base_url_2
				print("CDN URL {0} will be replaced by {1}".format(
					current_value, script['src']))
		file_obj = open(source, "w+")
		file_obj.write(str(soup))
		file_obj.close()

	def update_link_to_static(files):
		source = files
		soup = BeautifulSoup(open(source), "html.parser")
		for link in soup.findAll('link', {"href": True}):
			print()
			print("Parsing TAG {}".format(link))
			str_append = re.findall(r'"(.*?)"', str(link))
			if str_append[0]:
				current_value = link['href']
				link['href'] = static_base_url_1 + \
					str_append[0].split(cdn_base_url)[1] + static_base_url_2
				print("CDN URL {0} will be replaced by {1}".format(
					current_value, link['href']))
		file_obj = open(source, "w+")
		file_obj.write(str(soup))
		file_obj.close()

	for files in options.files:
		print("Parsing HTML {} ...".format(files))
		if options.target == "cdn":
			print("Target is cdn")
			update_script_to_cdn(files)
			update_link_to_cdn(files)
		else:
			print("Target is static")
			update_script_to_static(files)
			update_link_to_static(files)

if __name__ == "__main__":
	main()
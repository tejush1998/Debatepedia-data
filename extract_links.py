#Import all the links corresponding to all the categories of the debatepedia website. 
# Keep only the unique links.

from bs4 import *
import sys
import re
import os
import requests

def retrieve_links_from_file(filename):

	if not(os.path.isdir("category_links")):
		os.makedirs("category_links")

	links = open(filename, "rb")
	all_links = []
	source = "https://web.archive.org"
    
	for lines in links :

		print (lines)
		page = requests.get('https://web.archive.org/web/20200929225234/'+lines.decode('ASCII'))
		soup = BeautifulSoup(page.text, 'lxml')

		write_name = soup.find('h1').string[9:]
		write_name = re.sub("/","_", write_name)	
		write_file = open("category_links/" + write_name, "wb")

		h3_tags = soup.findAll('h3')	

		for i in h3_tags :
			if(i.string != 'From Debatepedia'):

				y = i.next_sibling.next_sibling

				for j in y:
					a_links = j.findAll('a')

					for l in a_links:
						new_link = source + l['href']+"\n"
						write_file.write(bytes(new_link, 'utf-8'))
						all_links.append(bytes(new_link, 'utf-8'))
						print(all_links)

	all_links = set(all_links)

	write_all_links = open("category_links/" + "all_links", "wb")
	
	for i in all_links:
		write_all_links.write(i)
		
def main():
	retrieve_links_from_file(sys.argv[1])

if __name__ == '__main__':
	main()

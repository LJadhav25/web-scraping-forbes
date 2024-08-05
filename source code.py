import requests
from bs4 import BeautifulSoup

# url = "https://www.codewithharry.com"
url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
# GET THE HTML
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

# PARSE THE HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)

# HTML TREE TRAVERSAL
title = soup.title
# print(type(soup)) #BeautifulSoup
# print(type(title.string)) # NavigableString
# print(type(title))  #tag

# get all the paragraphs from the website
paras = soup.find_all('p')
# print(paras)

# print(soup.find('p'))  # get first para only
# print(soup.find('p')['class'])  # get the class name in the paragraph

# find all the elements with the class text-sm
# print(soup.find_all("p", class_="text-sm"))

# get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())


# get all the anchors from the website
arch = soup.find_all('a')
all_links = set()
# print(arch)
for link in arch:
    if '#' != link.get('href'):
        # linktext = "https://en.wikipedia.org/wiki" +link.get('href')
        all_links.add(link)
        # print(linktext)


#markup  = "<p><!-- this is a comment --></p>"
#soup2 = BeautifulSoup(markup)
#print(soup2.p.string)
#print(type(soup2.p.string)) #<class 'bs4.element.Comment'>


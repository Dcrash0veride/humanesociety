from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
site = "http://www.nehumanesociety.org/adopt/dogs/"

uClient = uReq(site)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

pup_tml = page_soup.findAll("div", {'class':'pet-box col-xs-12 col-sm-6 col-md-6'})

filename = 'dogs.csv'

f = open(filename, "w")

headers = "dog_name, dog_id, bio, attributes"

f.write(headers + "\n")

for i in pup_tml:
    name = i.div.h3.text
    id = i.div.div.span.text
    comments = i.findAll('span', {'class': 'js__pet-webcomment'})
    comment = comments[0].text
    descriptions = i.findAll('span', {'class': 'js__pet-description'})
    bio = descriptions[0].text
    f.write(name + ',' + id + ',' + comment.replace(",", "") + "," +  bio.replace(",", "") + "\n")

f.close()



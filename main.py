# import dependencies
#   1) web client interface
#   2) web-data parser
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# helper method to clean strings
def clean_string(str):
    result = str.strip()
    result = result.replace("Regular price", "")
    result = result.replace("\n", "")
    result = result.replace(" ", "")
    return result

# site to be scraped
my_url = 'https://shop.macmillerswebsite.com/'

# initialize/open web client
uClient = uReq(my_url)
page_html = uClient.read() # snag the HTML
uClient.close() # just like a scanner, close that stuff

page_soup = soup(page_html, "html.parser") # use bs4 to parse page_html using its "html.parser"

# find specific items containers to scrape
containers = page_soup.findAll("div", {"class":"grid__item medium-down--one-half post-large--one-fifth"})

# prototyping the loop
#   item_name_html = containers[0].findAll("p", {"class":"grid-link__title"})
#   item_price_html = containers[0].findAll("p", {"class":"grid-link__meta"})
#   item_price = clean_string(item_price_html[0].text)

filename = "results.csv"
f = open(filename, "w") # open file in "w" write mode
headers = "item, price\n" 
f.write(headers)

# loop over all containers
for container in containers:
    # isolate the item name chunk
    item_name_html = container.findAll("p", {"class":"grid-link__title"})
    # save the inner text as variable
    item_name = item_name_html[0].text
    print(item_name)

    # isolate the item price chunk
    item_price_html = container.findAll("p", {"class":"grid-link__meta"})
    # save the inner text as variable
    item_price = clean_string(item_price_html[0].text)
    print(item_price)
    print("")

    f.write(item_name + "," + item_price + "\n") # write to the csv file, comma deliminated

f.close() # close filewrited

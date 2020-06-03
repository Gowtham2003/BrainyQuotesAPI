import requests
from bs4 import BeautifulSoup as bs

quotesDictionary = {
    "success":True,
    "data":[]
}

def getQuotes(query):
    BASE_URL = "https://www.brainyquote.com/"

    url = f"https://www.brainyquote.com/topics/{query}-quotes"

    r = requests.get(url)

    soup = bs(r.content,"lxml")
    divs = soup.findAll("div",{"class":"qll-bg"})

    for div in divs:
        quote = div.find("a",{"title":"view quote"}).text
        quotelink =  BASE_URL + div.find("a",{"title":"view quote"}).get("href")
        author =  "By " + div.find("a",{"title":"view author"}).text
        authorlink =  BASE_URL + div.find("a",{"title":"view author"}).get("href")

        tagsElement = div.findAll("a",{"class":"qkw-btn btn btn-xs oncl_list_kc"})
        tags = []
        for tag in tagsElement:
            tags += tag

        QuoteContent = {
            "quote":quote,
            "quotelink":quotelink,
            "author":author,
            "authorlink":authorlink,
            "tags":tags
        }

        quotesDictionary["data"].append(QuoteContent)

#    print(quotesDictionary)

#getQuotes("nature")

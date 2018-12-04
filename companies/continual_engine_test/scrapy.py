import re
import urllib
import argparse

from googlesearch import search
from bs4 import BeautifulSoup


def apply_colour_to_text(quote, alist):
    """
    Highlight the query words in the result. 
    """
    extrac_text = re.findall(r"\btypes of earthquakes\b", quote.text.lower().replace('\n          ', ''))
    if len(extrac_text) >= 1:
        apply_colour = "\033[44;33m{}\033[m".format(extrac_text[0])
        alist.append(quote.text.lower().replace('\n          ', '').replace("{}".format(extrac_text[0].lower()), apply_colour))
    return alist


def get_scrape_text(soup, alist):
    """
    Scrape the first website result 
    """
    table = soup.find('table', attrs={'id': 'Table_01'})
    for quote in table.select("p > span"):
        apply_colour_to_text(quote, alist)
    return alist


def get_text(soup, alist):
    """
    Scrape the second website result 
    """
    for quote in soup.find_all("p"):
        apply_colour_to_text(quote, alist)
    return alist


def get_website_text(soup, alist):
    """
    Scrape the third website result 
    """
    for quote in soup.find_all("td"):
        apply_colour_to_text(quote, alist)
    return alist


def web_scrape(url, stop):
    """
    Scrape the website results from all the websites
    """
    alist = []
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html5lib")
    if stop == 1:
        alist = get_scrape_text(soup, alist)
    elif stop == 2:
        alist = get_text(soup, alist)
    elif stop == 3:
        alist = get_website_text(soup, alist)
    return soup.title.text, alist


def main(query):
    result = {}
    stop = 1
    if not query:
        query = 'Types of earthquake'
    for url in search(query, tld="co.in", num=stop+1, stop=stop, pause=stop + 1):
        name, alist = web_scrape(url, stop)
        result[stop] = alist
        print str(stop) + ". " + name
        print url + " \n"
        stop += 1
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'query', type=str, help='Pass the query string')
    query = parser.parse_args().query
    result = main(query)
    for key, value in result.items():
        print "Highlight the query words: {}\n".format(key)
        if len(value) >= 1:
            for i in value:
                print i.encode("utf-8") + "\n".encode("utf-8")

"""This module has just the class implemented, nothing else."""

import re
import urllib2
from bs4 import BeautifulSoup

class IngatlanComParser(object):
    "Class definition for parsing ingatlan.com pages for listings"
    def __init__(self, url):
        if self.is_url_valid(url):
            self._start_url = self._url = url
        else:
            raise Exception("IngatlanComParser", "Invalid init url")

    def parse(self): # do I have to intorduce another def _parse(self) layer?
        "Method to iterate throug all the pages starting with self._start_url"
        url_items = []

        while self._url != "":
            url_soup = self.get_and_cook_content()

            # parse all listings
            for item in url_soup.find_all("div", class_="listing"):
                url_items.append({
                    "address": item.select("div.listing__address")[0].string,
                    "price": item.select("div.price")[0].string,
                    "link": "https://ingatlan.com/" + item["data-id"],
                })

            next_link_tag = url_soup.find_all("link", attrs={
                "rel": "next",
            })

            # find next url
            if len(next_link_tag) > 0:
                next_link_candidat = next_link_tag[0]["href"]
                if self.is_url_valid(next_link_candidat):
                    self._url = next_link_candidat
                elif self.is_url_valid("https:" + next_link_candidat):
                    self._url = "https:" + next_link_candidat
                else:
                    self._url = ""
                    raise Exception("IngatlanComParser", "Can't fetch next url on " + self._url)
            else:
                self._url = ""

        self._url = self._start_url
        return url_items

    def get_and_cook_content(self):
        "Method to get url content and cook it with BeautifulSoup"
        opener = urllib2.build_opener()
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

        return BeautifulSoup(opener.open(self._url).read(), 'html.parser')

    @staticmethod
    def is_url_valid(url):
        "Method to test, if the given URL passes class's \"requirements\""
        return re.search(r"http(s)?:\/\/(www.)?ingatlan.com\/([\w|\+|\/]*)(\?page=[0-9])?", url)

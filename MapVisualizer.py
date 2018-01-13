"""This module has just a class implemented, nothing else."""

import urllib2
import json
import os
import webbrowser

API_KEY = "AIzaSyDYhJgmIjXp-HPUbECydNXkPsXaQ4SYaB8"

class MapVisualizer(object):
    """MapVisualizer"""
    def __init__(self):
        self._mapitems = []

    def generate(self):
        """generate"""

        output_items = []
        for item in self._mapitems:
            output_items.append(item.data())

        json_dump = json.dumps(output_items)
        output_json = open("MapVisualizer.json", "w")
        output_json.write("data = '" + json_dump + "'")
        output_json.close()
        return json_dump

    def add(self, mapitem):
        """add"""
        if isinstance(mapitem, MapItem):
            self._mapitems.append(mapitem)
            return True
        else:
            raise Exception("MapVisualizer", "Cannot add to MapVisualizer non-MapItems")

    def display(self):
        """display"""
        webbrowser.open_new("file:///" + os.getcwd() + "/MapVisualizer.html")
        return True

class MapItem(object):
    """MapItem"""
    def __init__(self, link, price, address=None, latlng=None):
        if not (address or latlng) or not link or not price:
            raise Exception("MapItem", "Missing parameters")

        self._price = price
        self._link = link
        if address:
            self._address = address
            self._json = self.get_json()
            self._latlng = {
                "lat": self._json["results"][0]["geometry"]["location"]["lat"],
                "lng": self._json["results"][0]["geometry"]["location"]["lng"],
            }
            self._address = self._json["results"][0]["formatted_address"] # just te make everything consistent
        else:
            self._latlng = latlng # should be a dict: {"lat": 0.00, "lng": 0.00}
            self._json = self.get_json()
            self._address = self._json["results"][0]["formatted_address"]

    @staticmethod
    def normalise_address(address):
        """normalise_address"""
        return address.replace(" ", "+").encode("utf-8")

    def get_json(self, url=""):
        """get_json"""
        if url == "":
            if self._address:
                url_content = "address={}".format(self.normalise_address(self._address))
            else:
                url_content = "latlng={},{}".format(self._latlng["lat"], self._latlng["lng"])

        url = "https://maps.googleapis.com/maps/api/geocode/json?{}&key={}".format(url_content, API_KEY)

        return json.loads(urllib2.urlopen(url).read())

    def data(self):
        """data"""
        return {
            "price": self._price,
            "address": self._address,
            "latlng": self._latlng,
            "link": self._link,
        }

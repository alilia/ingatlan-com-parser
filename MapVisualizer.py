"""Please see the class descriptions for more information"""

import urllib2
import json
import os
import webbrowser

API_KEY = "AIzaSyDYhJgmIjXp-HPUbECydNXkPsXaQ4SYaB8" # you have found a candy

class MapVisualizer(object):
    "MapVisualizer is to create an object to contain a list or lists of MapItem objects. You can .generate() a JSON and .display() the default Google Maps map."
    def __init__(self):
        self._mapitems = [[]]

    def __add__(self, other):
        "When adding two instances of MapVisualizer, their mapitems are concatanated"
        mapitems_self = self.mapitems
        mapitems_other = other.mapitems
        self._mapitems = []

        if mapitems_self:
            for mapitems in mapitems_self:
                if mapitems:
                    self._mapitems.append(mapitems)

        if mapitems_other:
            for mapitems in mapitems_other:
                if mapitems:
                    self._mapitems.append(mapitems)

        return self

    def generate(self):
        "Generates JSON of mapitems"

        output_items = []
        def lets_get_deep(mapitems):
            """lets_get_deep"""
            for idx, value in enumerate(mapitems):
                if isinstance(value, list):
                    mapitems[idx] = lets_get_deep(value)
                else:
                    mapitems[idx] = value.data

            return mapitems

        output_items = lets_get_deep(self.mapitems)

        json_dump = json.dumps(output_items)
        output_json = open("MapVisualizer.json", "w")
        output_json.write("data = '" + json_dump + "'")
        output_json.close()
        return json_dump

    def add(self, mapitem):
        "Method to populate mapitems"
        if isinstance(mapitem, MapItem):
            self._mapitems[0].append(mapitem)
            return True
        elif isinstance(mapitem, list):
            for item in mapitem:
                if not isinstance(item, mapitem):
                    raise Exception("MapVisualizer", "Cannot add to MapVisualizer non-MapItems")

            self._mapitems.append(mapitem)
            return True
        else:
            raise Exception("MapVisualizer", "Cannot add to MapVisualizer non-MapItems")

    def display(self):
        "Displays Google Maps map in default browser"
        webbrowser.open_new("file:///" + os.getcwd() + "/MapVisualizer.html")
        return True

    @property
    def mapitems(self):
        "No comment"
        return self._mapitems

class MapItem(object):
    "MapItem is to contain all the necessary information for a listing to appear on a map. When initializing, it requests all the missing information from Google Maps API."
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
        "Formats address string for Google Maps API"
        return address.replace(" ", "+").encode("utf-8")

    def get_json(self, url=""):
        "Requests JSON information from Google Maps API"
        if url == "":
            if self._address:
                url_content = "address={}".format(self.normalise_address(self._address))
            else:
                url_content = "latlng={},{}".format(self._latlng["lat"], self._latlng["lng"])

        url = "https://maps.googleapis.com/maps/api/geocode/json?{}&key={}".format(url_content, API_KEY)

        return json.loads(urllib2.urlopen(url).read())

    @property
    def data(self):
        "No comment"
        return {
            "price": self._price,
            "address": self._address,
            "latlng": self._latlng,
            "link": self._link,
        }

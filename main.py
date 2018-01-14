"""Current Python code parses ingatlan.com links for all the listings, requests necessary inforamtion from Google Maps API and dumps it to a JSON. Some HTML/JS magic visualizes it on a Google Maps canvas."""

import IngatlanCom as ic
import MapVisualizer as mv

def populate_mapvisualizer(to_parse):
    "Creates, populates and returns a MapVisualizer object"
    mapvisualizer = mv.MapVisualizer()

    for item in to_parse:
        mapvisualizer.add(mv.MapItem(
            address=item["address"],
            price=item["price"],
            link=item["link"],
        ))

    return mapvisualizer

def main():
    "Welcome to the jungle"
    mapvisualizer = mv.MapVisualizer()

    urls_to_parse = [
        "https://ingatlan.com/budapest/kiado+garazs",
        "https://ingatlan.com/budapest/elado+garazs",
    ]

    for url in urls_to_parse:
        ingatlan_com = ic.IngatlanComParser(url)
        parsed_ingatlan_com = ingatlan_com.parse()
        retval = populate_mapvisualizer(parsed_ingatlan_com)
        mapvisualizer += retval

    mapvisualizer.generate()
    mapvisualizer.display()

    return False

main()
print "Done"

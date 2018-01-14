"""'sup my nigga"""

import IngatlanCom as ic
import MapVisualizer as mv

def populate_mapvisualizer(to_parse):
    """populate_mapvisualizer"""
    mapvisualizer = mv.MapVisualizer()

    for item in to_parse:
        mapvisualizer.add(mv.MapItem(
            address=item["address"],
            price=item["price"],
            link=item["link"],
        ))

    return mapvisualizer

def main():
    """welcome to the jungle"""
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

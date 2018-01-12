"""'sup my nigga"""

import IngatlanCom as ic
import MapVisualizer as mv

def main():
    """welcome to the jungle"""
    ingatlan_com = ic.IngatlanComParser("file:///Users/ifilin/Desktop/Kiado%CC%81%20gara%CC%81zsok%20Budapest%20-%20ingatlan.com.html")
    parsed_ingatlan_com = ingatlan_com.parse()

    map_visualiser = mv.MapVisualizer()
    for item in parsed_ingatlan_com:
        map_visualiser.add(mv.MapItem(
            address=item.address,
            price=item.price,
            link=item.link,
        ))

    map_visualiser.generate()
    map_visualiser.display()

    return False

main()

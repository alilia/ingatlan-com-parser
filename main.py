"""'sup my nigga"""

import IngatlanCom as ic
import MapVisualizer as mv

def main():
    """welcome to the jungle"""
    ingatlan_com = ic.IngatlanComParser("https://ingatlan.com/budapest/kiado+garazs")
    parsed_ingatlan_com = ingatlan_com.parse()

    map_visualiser = mv.MapVisualizer()
    for item in parsed_ingatlan_com:
        pass
    #     map_visualiser.add(mv.MapItem(
    #         address=item["address"],
    #         price=item["price"],
    #         link=item["link"],
    #     ))

    # map_visualiser.generate()
    # map_visualiser.display()

    return False

main()
print "Done"
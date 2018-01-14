Current Python code parses ingatlan.com links for all the listings, requests necessary inforamtion from Google Maps API and dumps it to a JSON. Some HTML/JS magic visualizes it on a Google Maps canvas.

# How to use it?

Populate ```urls_to_parse``` list in ```main.py``` with the links to parse and visualize. Run that file. After it finishes parsing all the pages, ```MapVisualizer.html``` will open in the default browser.

# Dependencies

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* basic Python 2.7 modules
  * json
  * os
  * re
  * urllib2
  * webbrowser

# Module descriptions

## ```MapVisualizer```

Module has two classes:

### ```MapVisualizer```

```MapVisualizer``` is to create an object to contain a list or lists of ```MapItem``` objects. You can ```.generate()``` a JSON and ```.display()``` the default Google Maps map.

### ```MapItem```

```MapItem``` is to contain all the necessary information for a listing to appear on a map. When initializing, it requests all the missing information from Google Maps API.

## ```IngatlanCom```

Module has one class implemented in it. It is a basic iterator and listing parser for ingatlan.com search result pages. Returns a ```list``` with all the found listings in it.

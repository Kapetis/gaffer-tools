import urllib2

data = """
{
    "elements": [
	{
	    "class": "gaffer.data.element.Edge",
	    "properties": {
		"name": {
  		    "gaffer.function.simple.types.FreqMap": {
                         "r:http://ex.org/#eats": 1,
                         "@r": 1
                    } 
                }
	    },
	    "group": "BasicEdge",
	    "source": "n:http://ex.org/#lion",
	    "destination": "n:http://ex.org/#zebra",
	    "directed": true
	},
	{
	    "class": "gaffer.data.element.Edge",
	    "properties": {
		"name": {
  		    "gaffer.function.simple.types.FreqMap": {
			"n:http://ex.org/#zebra": 1,
			"@n": 1
		    }
		}
	    },
	    "group": "BasicEdge",
	    "source": "n:http://ex.org/#lion",
	    "destination": "r:http://ex.org/#eats",
	    "directed": true
	}
    ]
}
"""

req = urllib2.Request('http://localhost:8080/graph/doOperation/add/elements')
response = urllib2.urlopen(req, data)
result = response.read()

print result


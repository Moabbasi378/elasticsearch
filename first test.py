"""
------------------------------------------------------------------------
just a test for elastic search
by mohammad abbasi
""pixend""
gimail : mohammadabbasi378@gmail.com
github : moabbasi378
------------------------------------------------------------------------
"""

from datetime import datetime
from elasticsearch import Elasticsearch

elasticsearch_server  = Elasticsearch("http://localhost:9200/") #Determine the elasticsearch server

liverpool_info = {     #Dict of information about each club for adding into the index in Elasticsearc
"name" : "liverpool fc",
"manager" : "jurgen klopp",
"stadium" : "anfield",
}

resp = elasticsearch_server.index(#build an index 
    index = "football",
    id = 1,
    document = liverpool_info #chose our dict as document
    )
print(resp['result'])

resp = elasticsearch_server.get( # recive our index 
    index = "football", 
    id=1
    )
print(resp['_source'])

elasticsearch_server.indices.refresh(
    index = "football"
    )

resp = elasticsearch_server.search(
    index = "football", 
    query = {"match_all": {}})

print("Got %d Hits:" % resp['hits']['total']['value'])

for hit in resp['hits']['hits']:
    print("%(name)s %(manager)s %(stadium)s" % hit["_source"])




















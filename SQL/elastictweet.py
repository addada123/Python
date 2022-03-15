# https://www.pg4e.com/code/elastictweet.py

# Example from:
# https://elasticsearch-py.readthedocs.io/en/master/

# pip3 install elasticsearch

# (If needed)
# https://www.pg4e.com/code/hidden-dist.py
# copy hidden-dist.py to hidden.py
# edit hidden.py and put in your credentials

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection

import hidden

secrets = hidden.elastic()

es = Elasticsearch(
    [secrets['host']],
    http_auth=(secrets['user'], secrets['pass']),
    url_prefix = secrets['prefix'],
    scheme=secrets['scheme'],
    port=secrets['port'],
    connection_class=RequestsHttpConnection,
)
indexname = "pg4e_bf813e65a9"

# Start fresh
# https://elasticsearch-py.readthedocs.io/en/master/api.html#indices
res = es.indices.delete(index=indexname, ignore=[400, 404])
print("Dropped index")
print(res)

res = es.indices.create(index=indexname)
print("Created the index...")
print(res)

doc = {
    'author': 'addada',
    'type' : 'tweet',
    'text': 'try to get you to see the big picture while we are defining the tiny',
    'timestamp': datetime.now(),

    'author2': 'addada2',
    'type2': 'tweet',
    'text': 'fragments that make up that big picture While the book is written',
    'timestamp2': datetime.now(),

    'author3': 'addada3',
    'type3': 'tweet',
    'text': 'linearly and if you are taking a course it will progress in a linear',
    'timestamp3': datetime.now(),

    'author4': 'addada4',
    'type4': 'tweet',
    'text': 'fashion dont hesitate to be very nonlinear in how you approach the',
    'timestamp4': datetime.now(),

    'author5': 'addada5',
    'type5': 'tweet',
    'text': 'material Look forwards and backwards and read with a light touch By',
    'timestamp5': datetime.now(),
}

# Note - you can't change the key type after you start indexing documents
res = es.index(index=indexname, id='abc', body=doc)
print('Added document...')
print(res['result'])

res = es.get(index=indexname, id='abc')
print('Retrieved document...')
print(res)

# Tell it to recompute the index - normally it would take up to 30 seconds
# Refresh can be costly - we do it here for demo purposes
# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-refresh.html
res = es.indices.refresh(index=indexname)
print("Index refreshed")
print(res)

# Read the documents with a search term
# https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html
x = {
  "query": {
    "bool": {
      "must": {
        "match": {
          "text": "backwards"
        }
      },
      "filter": {
        "match": {
          "type": "tweet"
        }
      }
    }
  }
}

res = es.search(index=indexname, body=x)
print('Search results...')
print(res)
print()
print("Got %d Hits:" % len(res['hits']['hits']))
for hit in res['hits']['hits']:
    s = hit['_source']
    print(f"{s['timestamp']} {s['author']}: {s['text']}")



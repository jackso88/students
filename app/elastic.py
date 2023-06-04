import elasticsearch
from app import es

def delete_by_id(index, id):
    result = es.search(index='docs', size=1, query={
            "match": {
                'id': id
            }
        })["hits"]["hits"]
    try:
        es.delete(index='docs', id=result[0]["_id"])
        return True
    except Exception:
       return False

def query_index_by_text(index, text):
    search = es.search(
        index='docs',
        size=20,
        query = {'multi_match': {'query': text, 'fields': ['*']}})
    print(search['hits']['hits'])
    ids = [hit['_source']['id'] for hit in search['hits']['hits']]
    if(len(ids) > 20):
        return ids[:20]
    return ids

def query_index_by_id(index, id):
    result = es.search(index='docs', size=1, query={
            "match": {
                'id': id
            }
        })["hits"]["hits"]
    return result

def add_to_index(index, model):
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    es.index(index=index, id=model.id, body=payload)


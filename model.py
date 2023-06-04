import asyncio
from elasticsearch import AsyncElasticsearch
import secrets
import string


def generate_id(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    return crypt_rand_string


async def async_search(es_object, index, search_object):
    resp = await es_object.search(index=index, body=search_object, size=5)
    return resp


async def async_create(es_object, index, body):
    id = generate_id(20)
    resp = await es_object.create(index=index, id=id, document=body)
    return [id, resp]


async def async_update(es_object, index, id, body):
    resp = await es_object.update(index=index, id=id, document=body)
    return [id, resp]


async def async_delete(es_object, index, id):
    try:
        resp = await es_object.delete(index=index, id=id)
        return "GOOOOOOOOOOOD"
    except:
        return "NOOOOOOOOOOOO"


async def search(request):
    value = request
    index = "tweets"
    search_object = {
        "query": {
            "match": {
                "text": f"{value}"
            }
        }
    }
    # Add your parameters of login and password to http_auth
    es = AsyncElasticsearch("http://localhost:9200", http_auth=('', ''))
    ret = await asyncio.create_task(async_search(es, index, search_object))
    return ret


async def create(request):
    value = request
    index = "tweets"
    es = AsyncElasticsearch("http://localhost:9200", http_auth=('', ''))
    ret = await asyncio.create_task(async_create(es, index, request))
    return ret


async def delete(request):
    id = request
    index = "tweets"
    es = AsyncElasticsearch("http://localhost:9200", http_auth=('', ''))
    ret = await asyncio.create_task(async_delete(es, index, id))
    return ret


async def update(request):
    body = request['id']
    id = request['val']
    index = "tweets"
    es = AsyncElasticsearch("http://localhost:9200", http_auth=('', ''))
    ret = await asyncio.create_task(async_update(es, index, id, body))
    return ret

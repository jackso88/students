from model import search, delete, update
import asyncio
import json
class SearchView():

    def __init__(self, request):
        self.request = request

    async def search(self):
        
        val = await search(self.request)
        response =  [{'id': item['_id'] , 
                'val':item['_source']} 
                for item in val['hits']['hits']]
        return response


class DeleteView():

    def __init__(self, request):
        self.request = request

    async def delete(self):
        response = await delete(self.request)
        return response        


class UpdateView():

    def __init__(self, request):
        self.request = request

    async def delete(self):
        response = await update(self.request)
        return [{
            'id': response[0],
            'val': response[1]
        }]


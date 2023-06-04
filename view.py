from validations import validation
from model import search, create, delete, update
import asyncio
import json


class SearchView():

    def __init__(self, request):
        self.request = request

    async def search(self):
        if validation(self.request):
            val = await search(self.request)
            response = [{'id': item['_id'],
                         'val': item['_source']}
                        for item in val['hits']['hits']]
            return response

        else:
            return None


class CreateView():

    def __init__(self, request):
        self.request = request

    async def create(self):
        if validation(self.request):
            response = await create(self.request)
            print(response)
            return [{
                'id': response[0],
                'val': response[1]
            }]

        else:
            return None


class DeleteView():

    def __init__(self, request):
        self.request = request

    async def delete(self):
        if validation(self.request):
            response = await delete(self.request)
            return response
        else:
            return None


class UpdateView():

    def __init__(self, request):
        self.request = request

    async def delete(self):
        if validation(self.request):
            response = await update(self.request)
            return [{
                'id': response[0],
                'val': response[1]
            }]
        else:
            return None

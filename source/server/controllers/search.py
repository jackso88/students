from source.database.index import connectToDataBase
from source.elasticSearch.index import connectToES
from constants import mongoCollection
from constants import elsasticIndex
import json

def searchRecords(searchLine):
    connection = connectToDataBase()
    elasticSearch = connectToES()
    resultOfSearch = elasticSearch.search(elsasticIndex, searchLine)
    hits = resultOfSearch["hits"]["hits"]
    idArray = map(lambda document: document["_id"], hits)
    arrayOfPosts = sorted(connection.findById(mongoCollection, idArray), key=lambda x: x["created_date"])
    return json.dumps({elsasticIndex: arrayOfPosts})
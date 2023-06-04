from source.database.index import connectToDataBase
from source.elasticSearch.index import connectToES
from constants import mongoCollection
from constants import elsasticIndex
import json

def deleterRecord(id):
    connection = connectToDataBase()
    elasticeSearch = connectToES()
    record = connection.findOneById(mongoCollection, id)
    record["_id"]=id
    connection.deleteRecord(mongoCollection, id)
    elasticeSearch.delete(elsasticIndex, id)
    return json.dumps({ "deletedRecord": record})

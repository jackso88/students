from source.csvFile.csvFileReader import CsvFileReader
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDatabase:

    def __init__(self, connectionString, databaseName):
        self.connectionString = connectionString
        self.database = MongoClient(self.connectionString)[databaseName]

    def insertDocument(self, collectionName, document):
        collection = self.database[collectionName]
        collection.insert_one(document)

    def readCsvFile(self, fileName, collectionName, currectionFunction):
        collection = self.database[collectionName]
        reader = CsvFileReader(fileName)
        for document in reader.rowStreamGenerator():
           collection.insert_one(currectionFunction(document))

    def createDatabaseGenerator(self, collectionName):
        collection = self.database[collectionName]
        def generator():
            for row in collection.find():
                yield row
        return generator

    def findById(self, collectionName, idArray):
        collection = self.database[collectionName]
        result = []
        for id in idArray:
            document = collection.find_one({"_id":ObjectId(id)})
            document["_id"]=str(document["_id"])
            result.append(document)
        return result

    def findOneById(self, collectionName, id):
        collection = self.database[collectionName]
        return collection.find_one({"_id":ObjectId(id)})

    def deleteRecord(self,collectionName, recordId):
        collection = self.database[collectionName]
        collection.delete_one({"_id": ObjectId(recordId)})


        


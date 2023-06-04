from source.elasticSearch.index import connectToES
from source.database.index import connectToDataBase
from constants import elsasticIndex
from constants import mongoCollection

connectionES = connectToES()
databaseConnection = connectToDataBase()

connectionES.createIndex(elsasticIndex, databaseConnection.createDatabaseGenerator(mongoCollection))

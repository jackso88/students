from source.database.mongoDatabase import MongoDatabase
from source.elasticSearch.elasticSearch import ElasticSeacrhForDatabase
from constants import serverPort
from source.server.index import runServer

runServer(serverPort)



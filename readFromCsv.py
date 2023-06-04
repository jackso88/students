from sys import argv
import os.path
from source.database.index import writeRecordsFromCsvFile

filePath = argv[1]

if(not os.path.exists(filePath)):
    raise Exception("There is not file with name \""+ filePath+"\"")

writeRecordsFromCsvFile(filePath)

import csv
from os import path

class CsvFileReader:
    
    def __init__(self, fileName):
        self.filName = path.abspath(fileName)

    def createCsvReader(self):
        file = open(self.filName, encoding='utf-8')
        return csv.reader(file, delimiter = ",")

    def readAll(self):
        result = {}
        result['rows'] = []
        fileReader = self.createCsvReader(self)
        for row in fileReader:
            if "headers" not in result:
                result["headers"] = row
            else:
                result['rows'].append(row)
        return result

    def rowStreamGenerator(self):
        fileReader = self.createCsvReader()
        headers = []
        for row in fileReader:
            if  len(headers) == 0:
                headers = row
            else:
                document = dict(zip(headers, row))
                yield document


    

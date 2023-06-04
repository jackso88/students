import sqlite3
from elasticsearch import Elasticsearch


conn = sqlite3.connect('app.db')
cursor = conn.cursor()


es = Elasticsearch(hosts=["http://127.0.0.1:9200"])


for row in cursor.execute('SELECT id, text, created_date, rubrics FROM docs'):
    document = {col[0]: row[i] for i, col in enumerate(cursor.description)}
    es.index(index='docs', body=document)
    
conn.close()

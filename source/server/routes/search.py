from flask import Blueprint
from flask import request
from source.server.controllers.search import searchRecords

searchRoute = Blueprint('routeSearch', __name__)


@searchRoute.route('/search', methods=['GET'])
def searchDocuments():
    """
  ---
  get:
    summary: 'ищет нужный параметр'
    parameters:
      - in: query
        name: query
        required: true
        schema:
          type: str
        description: 'строка для поиска 20 документов' 
    responses:
      '200':
        description: 'Удален нужный документ'
        content:
          application/json:
            result:
                decription: 'Удаленный документ'
    tags:
    """
    return searchRecords(request.args["query"])

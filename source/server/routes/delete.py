from flask import Blueprint
from source.server.controllers.delete import deleterRecord

deleteRoute = Blueprint('routeDelete', __name__)


@deleteRoute.route('/document/<id>', methods=['DELETE'])
def delete(id):
    """
   ---
   delete:
     summary: 'удаляет по id'
     parameters:
       - in: path
         name: id
         required: true
         schema:
          type: integer
          minimum: 1
         description: 'id для поиска нужного документы, который нужно удалить' 

     responses:
       '200':
         description: '20 документов, соответсвующих поиску'
         content:
           application/json:
            result:
                decription: 'массив документов'
     tags:
    """
    return deleterRecord(id)
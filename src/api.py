import json
from flask import Flask, Response, jsonify, request, redirect, send_from_directory
from cfg_parser import get_config

from create_docs import get_apispec
from swagger import swagger_ui_blueprint, SWAGGER_URL


class API:
    def __init__(self, database, index):
        config = get_config('../config.ini')
        server_cfg = config['server']

        self.database = database
        self.index = index
        self.app = Flask(__name__)
        self.docs = None

        self.app.register_blueprint(
            swagger_ui_blueprint, url_prefix=SWAGGER_URL)

        @self.app.errorhandler(404)
        def resource_not_found(e):
            return jsonify(error=str(e)), 404

        @self.app.route('/', methods=['GET'])


        @self.app.route('/api/search', methods=['GET'])
        def search():
            """
            ---
            get:
                summary: Поиск записей
                description: Поиск документов по ключевым словам и возвращает 20 результатов, отсортированных по дате создания по возрастанию
                parameters:
                - in:query
                    name:search
                    schema:SearchParametersSchema
                responses:
                    '200':
                        description: ok
                        content:
                            application/json:
                                schema: SearchResponseSchema
                tags:
                - API
            """
            query = request.args.get("q", default="", type=str)
            results = self.index.search(
                query, size=20, source=True, source_includes=['id'], sort=[{"created_date": {"order": "asc"}}])

            result = []
            for res in results:
                result.append(self.database.get_by_id(res['id']))

            return jsonify(result)

        @self.app.route('/api/delete/<id>', methods=['DELETE'])
        def delete(id):
            """
            ---
            delete:
                summary: Удаление записи
                description: Удаляет документ по полю  `id`
                parameters:
                - in:path
                    name:delete
                    schema:DeleteParametersSchema
                responses:
                    '200':
                        description: ok
                        content:
                            application/json:
                                schema: DeleteSuccessSchema
                    '404':
                        description: error
                        content:
                            application/json:
                                schema: DeleteErrorSchema
                tags:
                - API
            """
            try:
                self.index.delete_by_id(id)
                self.database.delete_by_id(id)

                return Response(response="{'message':'success'}", status=200, mimetype='application/json')
            except:
                return Response(response="{'message':'error'}", status=404, mimetype='application/json')

        @self.app.route('/search')
        def search_front():
            """
            ---
            get:
                summary: Поиск
                description: Поиск
                responses:
                    '200':
                        description: ok
                        content:
                            text/html:
                                schema: SearchPageSchema
                tags:
                - frontend
                """
            return send_from_directory('', 'search.html')

        @self.app.route('/swagger')
        def create_swagger_spec():
            return json.dumps(self.docs.to_dict())

        self.docs = get_apispec(self.app)

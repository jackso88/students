from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from source.server.routes.search import searchDocuments
from source.server.routes.delete import delete
from source.server.index import createServer
import json

app = createServer()

def load_docstrings(spec):
    with app.app_context():
        spec.path(view=searchDocuments)
        spec.path(view=delete)
    pass


def get_apispec():
    """ Формируем объект APISpec.

    :param app: объект Flask приложения
    """
    spec = APISpec(
        title="Document searcher",
        version="1.0.0",
        openapi_version="3.0.3",
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
    )
    load_docstrings(spec)
    return spec

def saveServerDocumentation():
    spec = get_apispec()
    with open('./docs.json','w') as file:
        json.dump(spec.to_dict(), file, indent=2, ensure_ascii=False,)

saveServerDocumentation()
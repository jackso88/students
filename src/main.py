from src.cfg_parser import get_config
from src.index import Index
from src.database import Database
from src.api import API
def init():
    api = API(Database(), Index())
    return api
def populate_db(api: API, filepath):
    api.database.parse_to_db(filepath)
def make_index(api: API):
    api.index.index_database(api.database)
def main(api: API):
    config = get_config('../config.ini')
    api.app.run(port=config['server']['port'])
if __name__ == "__main__":
    api = init()                
    populate_db(api, "../posts.csv")
    make_index(api)
    main(api)
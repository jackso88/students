from sqlalchemy.orm import Session
from models import Post
from elastic import MyElastic

my_elastic = MyElastic()

def search_post_by_text(db: Session, search_text: str):
    id_list = [item["id"] for item in my_elastic.search_by_text(search_text)]
    result = db.query(Post) \
        .filter(Post.id.in_(id_list)) \
        .order_by(Post.created_date.desc()) \
        .all()
    return result

def delete_by_id(db: Session, id: int) -> bool:
    delete_item = my_elastic.search_by_id(id)
    if delete_item is not None:
        elastic_result = my_elastic.delete_by_id(delete_item[0]["_id"])
        db_result = bool(db.query(Post).filter(Post.id == id).delete())
        db.commit()
        return all((elastic_result, db_result))
    return False

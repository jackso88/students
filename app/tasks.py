from app import db, es
from elastic import delete_by_id, query_index_by_text, query_index_by_id, add_to_index

async def search(Model, text):
    ids = query_index_by_text('docs', text)
    docs = []
    for i in ids:
        docs.extend(query_index_by_id('docs', i))
    docs_sorted = sorted(docs, key=lambda x: x["_source"]["created_date"])
    texts = [i["_source"]["text"] + i["_source"]["created_date"] for i in docs_sorted]
    texts = "<pre>\n\n</pre>".join(texts)
    return texts

    """if not es.indices.exists(index='docs'):
        for post in Model.query.all():
            add_to_index('docs', post)
    if text is None:
        return "Text is None"
    try:
        ids = query_index_by_text('docs', text)
        result = Model.query.filter(Model.id.in_(ids)).order_by(Model.created_date.desc()).all()
        return {"result": [post.as_dict() for post in result]}
    except Exception as exc:
        return str(exc)"""

async def delete(Model, id):
    delete_item = query_index_by_id('docs', id)
    if delete_item is not None:
        elastic_result = delete_by_id('docs', id)
        if elastic_result is True:
            db.session.commit()
            return "Deleted"
    return "Not Found"
    """
    if not es.indices.exists(index='docs'):
        for post in Model.query.all():
            add_to_index('docs', post)
    delete_item = query_index_by_id('docs', id)
    if delete_item is not None:
        elastic_result = delete_by_id('docs', id)
        if elastic_result is True:
            db_result = bool(Model.query.filter(Model.id==id).delete())
            db.session.commit()
            return str(db_result)
        return "Not found post with such id"
    return "Not found post with such id"
    э"""

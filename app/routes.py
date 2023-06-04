from app import app, loop, db
from flask import request
from models import Docs
from tasks import search, delete

@app.get('/search/')
def get_posts():
    text = request.args["text"]
    result = loop.run_until_complete(search(Docs, text))
    return result

@app.get('/delete/')
def delete_post():
    id = request.args["id"]
    result = loop.run_until_complete(delete(Docs, id))
    return result

"""
@app.route('/del/<int:id>', methods=['POST'])
def delete_resource(id):
    #resource = db.query.get_or_404(id)
    
    #db.session.delete(resource)
    #db.session.commit()
    
    return jsonify({'message': 'Resource deleted'})"""


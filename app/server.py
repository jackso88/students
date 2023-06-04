from app import app
import models, routes
import elastic

if __name__ == '__main__':
    app.run(host='0.0.0.0')

from flask_restful import Api
from Document import Document_CRUD

def init_resources(app):
    api = Api(app)
    api.add_resource(Document_CRUD, '/document')
    return app
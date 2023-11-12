from flask import Blueprint
from flask_restx import Api

from blueprints.documented_endpoints.hello_world import namespace as hello_world_ns
from blueprints.documented_endpoints.entities import namespace as entities_ns
from blueprints.documented_endpoints.jinja_template import (
    namespace as jinja_template_ns,
)

blueprint = Blueprint("documented_api", __name__, url_prefix="/documented_api")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api_extension = Api(
    blueprint,
    title="Example api",
    version="1.0",
    authorizations=authorizations,
    description="Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation",
    doc="/doc",
)

api_extension.add_namespace(hello_world_ns)
api_extension.add_namespace(entities_ns)
api_extension.add_namespace(jinja_template_ns)

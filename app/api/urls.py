from flask import request, Blueprint
from flask.views import MethodView

from app.api.views import HelloWorldView, ItemView, StoreView

api = Blueprint("api", __name__, url_prefix='/api/<version>/')


class HelloWorld(MethodView):
    def get(self, version):
        return HelloWorldView().get_hello_world(request, version)


class Item(MethodView):
    def post(self, version):
        return ItemView().add_item(request, version)


class Store(MethodView):
    def post(self, version):
        return StoreView().register_store(request, version)


api.add_url_rule("/helloWorld", view_func=HelloWorld.as_view('helloWorld'))

# needed apis

api.add_url_rule("/addItem", view_func=Item.as_view('itemView'))
api.add_url_rule("/registerStore", view_func=Store.as_view('StoreView'))

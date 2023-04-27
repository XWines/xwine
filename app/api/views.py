from app.common.base_response import BaseResponse
from app.services.item import Item
from app.services.store import Store


class HelloWorldView:
    def get_hello_world(self, request, api_version='v1'):
        return BaseResponse().set_success_response({'a': 'hello world'}), 200


class ItemView:
    def add_item(self, request, api_version='v1'):
        item_id = request.json.get('itemId')
        item_type = request.json.get('itemType')
        if item_id == '' or item_type == '':
            return BaseResponse().set_error_response({'error_message': 'item id or item type can not be null'})
        return Item(item_id=item_id, item_type=item_type).add_item()


class StoreView:
    def register_store(self, request, api_version='v1'):
        data = request.json
        store_name = data.get('storeName')
        store_own_name = data.get('storeOwnName')
        store_own_f_name = data.get('storeOwnFatherName')
        if store_name == '' or store_own_name == '' or store_own_f_name == '':
            return BaseResponse().set_error_response(
                {'error_message': 'store name, store owner name, store owner father name any of them can not be null'})
        return Store(store_name=store_name, store_owner_name=store_own_name,
                     store_owner_f_name=store_own_f_name).register_store()

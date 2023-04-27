import traceback

from app import AppLogger
from app.common.base_response import BaseResponse
from app.models.xwine import Items

LOG = AppLogger()


class Item:
    def __init__(self, item_id, item_type):
        self.item_id = item_id
        self.item_type = item_type

    def is_item_exist(self):
        existing_items = Items.fetch_all_items()
        for item in existing_items:
            if item.item_type.lower() == self.item_type.lower():
                return True, item.item_id
        return False, 0

    def add_item(self):
        try:
            ok, item_id = self.is_item_exist()
            if ok:
                return BaseResponse().set_error_response(
                    {
                        'error_message': f"This item is already present with item id {item_id}, No need to "
                                         f"add again"})

            Items.insert_item(item_id=self.item_id, item_type=self.item_type)
            return BaseResponse().set_success_response(data_body={}, message='Item Added Successfully')

        except Exception as e:
            tb = traceback.format_exc()
            LOG.error(f"Adding item exception : {tb}, item_id : {self.item_id}, item_type: {self.item_type}")
            return BaseResponse().set_error_response({'error_message': f"Failed adding item error {e}"})

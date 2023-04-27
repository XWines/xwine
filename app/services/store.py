import uuid

from app import AppLogger
from app.common.base_response import BaseResponse
from app.models.xwine import Stores
import traceback

LOG = AppLogger()


class Store:
    def __init__(self, store_name, store_owner_name, store_owner_f_name):
        self.store_name = store_name
        self.store_owner_name = store_owner_name
        self.store_owner_f_name = store_owner_f_name

    def register_store(self):
        store_id = str(uuid.uuid4().hex)
        try:
            Stores.register_store(store_id=store_id, store_name=self.store_name, store_own_name=self.store_owner_name,
                                  store_own_father_name=self.store_owner_f_name)
            return BaseResponse().set_success_response(data_body={}, message='Store Registered Successfully')

        except Exception as e:
            tb = traceback.format_exc()
            LOG.error(f"Registering store exception : {tb}, store_id : {store_id}")
            return BaseResponse().set_error_response({'error_message': f"Failed registering store  error {e}"})

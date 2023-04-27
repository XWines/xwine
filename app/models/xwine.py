from datetime import datetime

from app import mongo


class BaseModel(mongo.Document):
    created = mongo.DateTimeField(default=datetime.utcnow)
    updated = mongo.DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated = datetime.utcnow()
        return super(BaseModel, self).save(*args, **kwargs)

    meta = {'abstract': True}


class Items(BaseModel):
    item_id = mongo.IntField(index=True)
    item_type = mongo.StringField(required=False, unique_with='item_id')

    @classmethod
    def insert_item(cls, **kwargs):
        cls.objects.create(**kwargs)

    @classmethod
    def fetch_all_items(cls):
        return cls.objects.filter().order_by('id')


class Stores(BaseModel):
    store_id = mongo.StringField(index=True)
    store_name = mongo.StringField(required=True)
    store_own_name = mongo.StringField(required=True)
    store_own_father_name = mongo.StringField(required=True)

    @classmethod
    def register_store(cls, **kwargs):
        cls.objects.create(**kwargs)

    def fetch_store_info(cls, store_id):
        return cls.objects.filter(store_id=store_id)

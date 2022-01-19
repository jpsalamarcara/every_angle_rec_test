
from mongoengine import *


class StoredItem(DynamicDocument):
    uid = SequenceField(primary_key=True)
    name = StringField(required=True)
    media_type = StringField(required=True)
    location = StringField()
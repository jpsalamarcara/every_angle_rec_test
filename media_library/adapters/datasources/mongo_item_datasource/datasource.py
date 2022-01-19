from typing import List

from .mongo.model import StoredItem
from media_library.core.datasources.item_datasource import ItemDataSource
from media_library.core.domain.item import Item


class MongoItemDataSource(ItemDataSource):

    def __init__(self):
        self.storage = StoredItem

    def save(self, item: Item):
        row = self.storage.objects(uid=item.uid).first() if item.uid is not None else None
        if row is None:
            row = self.storage(name=item.name,
                               media_type=item.media_type,
                               location=item.location
                               )
        else:
            row.update(**{'name': item.name, 'media_type': item.media_type, 'location': item.location})
        row.save()

    def __parse__(self, item: StoredItem) -> Item:
        return Item(uid=item.uid, name=item.name, media_type=item.media_type, location=item.location)

    def get(self, name: str = None, media_type: str = None, location: str = None) -> List[Item]:
        query = {}
        if name:
            query['name'] = name
        if media_type:
            query['media_type'] = media_type
        if location:
            query['location'] = location
        return [self.__parse__(row) for row in self.storage.objects(**query).all()]

    def delete(self, item: Item):
        row = self.storage.objects(uid=item.uid).first() if item.uid is not None else None
        if row:
            row.delete()

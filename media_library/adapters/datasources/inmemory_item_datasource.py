import copy
from typing import List

from media_library.core.datasources.item_datasource import ItemDataSource
from media_library.core.domain.item import Item


class InMemoryItemDataSource(ItemDataSource):

    def __init__(self):
        self.storage = {}
        self.last_key = 0

    def save(self, item: Item):
        to_store = copy.deepcopy(item)
        to_store.uid = self.last_key
        self.storage[self.last_key] = to_store
        self.last_key += 1

    def __cursor__(self):
        for k, v in self.storage.items():
            yield v

    def __filter_data__(self, filters: dict):
        no_filters = len(filters) == 0
        for row in self.__cursor__():
            matches = 0
            for field, value in filters.items():
                if getattr(row, field) == value:
                    matches += 1
            if no_filters or matches == len(filters):
                yield row

    def get(self, name: str = None, media_type: str = None, location: str = None) -> List[Item]:
        query = {}
        if name:
            query['name'] = name
        if media_type:
            query['media_type'] = media_type
        if location:
            query['location'] = location
        return [x for x in self.__filter_data__(query)]

    def delete(self, uid):
        assert uid is not None
        del self.storage[uid]

from injector import singleton, Injector
from mongoengine import connect

from media_library import SETUP
from media_library.adapters.datasources.inmemory_item_datasource import InMemoryItemDataSource
from media_library.adapters.datasources.mongo_item_datasource.datasource import MongoItemDataSource
from media_library.core.datasources.item_datasource import ItemDataSource


def item_datasource_factory():
    if SETUP.DATASOURCE == 'INMEMORY':
        return InMemoryItemDataSource()
    elif SETUP.DATASOURCE == 'MONGO':
        connect(host=SETUP.MONGODB_URL)
        return MongoItemDataSource()
    else:
        raise ValueError('Unsupported datasource!')


def configure(binder):
    binder.bind(ItemDataSource, to=item_datasource_factory, scope=singleton)


default_injector = Injector(configure)

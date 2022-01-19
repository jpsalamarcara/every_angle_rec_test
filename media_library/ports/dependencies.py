from injector import singleton, Injector

from media_library.core.datasources.item_datasource import ItemDataSource
from media_library.adapters.datasources.inmemory_item_datasource import InMemoryItemDataSource


def configure(binder):
    binder.bind(ItemDataSource, to=InMemoryItemDataSource, scope=singleton)


default_injector = Injector(configure)
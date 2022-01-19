import pytest

from media_library.core.datasources.item_datasource import ItemDataSource
from media_library.core.domain.item import Item
from media_library.ports.dependencies import default_injector


@pytest.fixture(scope='module')
def datasource() -> ItemDataSource:
    instance = default_injector.get(ItemDataSource)
    return instance


@pytest.fixture(scope='module')
def item():
    return Item(name='The Avengers', media_type='movie', location='file:///home/juan/media/the_avengers.mp4')


@pytest.fixture(scope='module')
def saved(datasource, item):
    datasource.save(item)
    return True


@pytest.fixture(scope='module')
def retrieved(datasource, item):
    items = datasource.get(name=item.name)
    return items[0]


def test_save(saved):
    assert saved


def test_get(retrieved, item):
    assert isinstance(retrieved, Item)
    assert item.name == retrieved.name
    assert item.media_type == retrieved.media_type
    assert item.location == retrieved.location
    assert item.uid is None
    assert retrieved.uid is not None


def test_delete(datasource, retrieved):
    datasource.delete(retrieved)
    items = datasource.get(name=retrieved.name, media_type=retrieved.media_type, location=retrieved.location)
    assert len(items) == 0


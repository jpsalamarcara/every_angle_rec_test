import abc
from typing import List

from media_library.core.domain.item import Item


class ItemDataSource(abc.ABC):

    @abc.abstractmethod
    def save(self, item: Item):
        pass  # pragma: no cover

    @abc.abstractmethod
    def get(self, name: str = None, media_type: str = None, location: str = None) -> List[Item]:
        pass  # pragma: no cover

    @abc.abstractmethod
    def delete(self, uid):
        pass  # pragma: no cover

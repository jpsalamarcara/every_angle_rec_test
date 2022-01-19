_AVAILABLE_MEDIA_TYPES = ('game', 'music', 'movie')


class Item:

    def __init__(self, uid=None, name: str = None, media_type: str = None, location: str=None):
        assert name is not None, 'name must have a value'
        assert media_type in _AVAILABLE_MEDIA_TYPES, 'media_type not yet supported!'
        assert location is not None, 'location must have a value'
        self.uid = uid
        self.name = name
        self.media_type = media_type
        self.location = location

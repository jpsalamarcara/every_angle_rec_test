import os


class ConfigEnv:

    def __init__(self):
        self.__load_env__()

    def __load_env__(self):
        self.MONGODB_URL = os.environ.get('MONGODB_URL', 'mongomock://localhost')
        self.DATASOURCE = os.environ.get('DATASOURCE', 'MONGO')
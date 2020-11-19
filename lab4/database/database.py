class DatabaseMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(DatabaseMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=DatabaseMeta):
    def __init__(self, path):
        self.__path = path

    def check_connection(self):
        try:
            file = open(self.__path, 'r')
            file.close()
            return True
        except Exception as ex:
            return False

    def select_users(self):
        if not self.check_connection():
            return None

        data = None
        with open(self.__path, 'r') as conn:
            data = conn.read().split('\n')

        return data

    def add_user(self, *args):
        if not self.check_connection():
            return None

        with open(self.__path, 'a') as conn:
            conn.write(' '.join(args))

        return args

    def delete_user(self, since=0, limit=1):
        if not self.check_connection():
            return None

        data = None
        with open(self.__path, 'r') as conn:
            data = conn.read().split('\n')

        delete_data = data[since:since + limit]
        for item in delete_data:
            data.remove(item)
        with open(self.__path, 'w') as conn:
            conn.write('\n'.join(data))

        return data

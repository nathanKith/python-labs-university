from commands.command import Command
from database.database import Database


class Delete(Command):
    def __init__(self, path, since=0, limit=1):
        self.__path = path
        self.__since = since
        self.__limit = limit

    def execute(self):
        db = Database(self.__path)
        if not db.check_connection():
            return None

        data = db.delete_user(self.__since, self.__limit)
        return data

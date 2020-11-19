from commands.command import Command
from database.database import Database


class Select(Command):
    def __init__(self, path):
        self.__path = path

    def execute(self):
        db = Database(self.__path)
        if not db.check_connection():
            return None

        return db.select_users()

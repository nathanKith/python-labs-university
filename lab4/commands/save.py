from commands.command import Command
from database.database import Database
from user.user import User


class Save(Command):
    def __init__(self, path, user):
        self.__path = path
        self.__user = user

    def execute(self):
        db = Database(self.__path)
        if not db.check_connection():
            return None

        data = db.add_user(*self.__user.unmarshal())
        return User(data[0], data[1], data[2])

from commands.invoker import Invoker
from commands.save import Save
from commands.delete import Delete
from commands.select import Select
from user.user import User


class App:
    def __init__(self, path):
        self.__path = path
        self.__invoker = Invoker()
        self.__save = None
        self.__delete = None
        self.__select = None

    def save(self, name, telephone, age):
        user = User(name, telephone, age)
        self.__save = Save(self.__path, user)
        self.__invoker.set_command(self.__save)
        return self.__invoker.invoke()

    def delete(self, since=0, limit=1):
        self.__delete = Delete(self.__path, since, limit)
        self.__invoker.set_command(self.__delete)
        return self.__invoker.invoke()

    def select(self):
        self.__select = Select(self.__path)
        self.__invoker.set_command(self.__select)
        data = self.__invoker.invoke()
        result = []
        if data:
            for item in data:
                user_data = item.split(' ')
                result.append(User(user_data[0], user_data[1], user_data[2]))
        return data

class Invoker:
    def __init__(self):
        self.__command = None

    def set_command(self, command):
        self.__command = command

    def invoke(self):
        if not self.__command:
            return self.__command.execute()

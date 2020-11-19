class User:
    def __init__(self, name, telephone, age):
        self.name = name
        self.telephone = telephone
        self.age = age

    def unmarshal(self):
        data = list()
        data.append(self.name)
        data.append(self.telephone)
        data.append(self.age)
        return data

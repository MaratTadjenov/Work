class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def inform_list(self):
        print(self.name, self.age)

c= Cat ('siam', 5)
c.inform_list()

class Home (Cat):
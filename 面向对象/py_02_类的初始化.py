class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s在吃鱼' % self.name)

    def drink(self):
        print('%s在喝水' % self.name)

tom = Cat('Tom')
tom.eat()
tom.drink()
class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s在吃鱼' % self.name)

    def drink(self):
        print('%s在喝水' % self.name)

    def __del__(self):
        print('%s挂了' % self.name)

    def __str__(self):
        """必须返回字符串格式"""
        return '我是小猫%s' % self.name

tom = Cat('Tom')
tom.eat()
tom.drink()
print(tom)
del tom

print('-' * 50)
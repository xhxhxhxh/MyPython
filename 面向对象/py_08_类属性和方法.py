class Person():
    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)

    @staticmethod # 静态方法
    def say_hello():
        print('你好')

    def __init__(self, name):
        self.name = name
        Person.count += 1

xiaoming = Person('小明')
xiaowang = Person('小王')
# print(Person.count)
Person.show_count()
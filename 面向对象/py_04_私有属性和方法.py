class Women():

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print('我叫%s，今年%d岁' % (self.name, self.__age))

xiaohong = Women('小红', 18)
# print(xiaohong.__age)
# xiaohong.__secret()

print(xiaohong._Women__age)
xiaohong._Women__secret()
class Anmial():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('吃')
    
    def drink(self):
        print('喝')
    
    def sleep(self):
        print('睡')


class Dog(Anmial):

    def shut(self):
        print('%s在叫' % self.name)


class Xiaotianquan(Dog):

    def shut(self): # 重写
        print('汪')
        super().shut()

ahuang = Dog('阿黄')
ahuang.sleep()
ahuang.eat()
ahuang.shut()

xiaotianquan = Xiaotianquan('阿黄')
xiaotianquan.shut()
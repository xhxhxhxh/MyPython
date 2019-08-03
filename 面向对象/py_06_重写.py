class Anmial():

    def eat(self):
        print('吃')
    
    def drink(self):
        print('喝')
    
    def sleep(self):
        print('睡')


class Dog(Anmial):

    def shut(self):
        print('叫')


class Xiaotianquan(Dog):

    def shut(self): # 重写
        print('汪')
        super().shut()

ahuang = Dog()
ahuang.sleep()
ahuang.eat()
ahuang.shut()

xiaotianquan = Xiaotianquan()
xiaotianquan.shut()
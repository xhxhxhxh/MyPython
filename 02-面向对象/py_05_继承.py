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


ahuang = Dog()
ahuang.sleep()
ahuang.eat()
ahuang.shut()
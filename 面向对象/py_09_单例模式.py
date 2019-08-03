class Person():
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        
        return cls.instance

    def __init__(self, name):
        self.name = name
       

xiaoming = Person('小明')
xiaowang = Person('小王')
print(xiaoming, xiaowang)
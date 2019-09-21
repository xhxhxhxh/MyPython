class Classmate():
    def __init__(self):
        self.name = []
        self.count = 0
    
    def add(self, name):
        self.name.append(name)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < len(self.name):
            name = self.name[self.count]
            self.count += 1
            return name
        else:
            raise StopIteration

classmate = Classmate()
classmate.add('张三')
classmate.add('李四')
classmate.add('王五')
classmate.add('赵六')

for name in classmate:
    print(name)



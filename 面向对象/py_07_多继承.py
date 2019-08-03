class A:

    def test(self):
        print('我是A')

class B:

    def test2(self):
        print('我是B')


class C(A, B):
    pass


person = C()
person.test()
person.test2()

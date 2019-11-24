class T1():
    def add(self):
        print('T1')

class T2(T1):
    pass

class T3(T1):
    pass


class T(T2, T3):
    pass

t = T()
print(T.__mro__)


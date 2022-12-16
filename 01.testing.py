import this

from DjangoFirst.firstApp import models


class Hello(models.Model):
    a = ""
    b = 1
    def __init__(self,a,b):
        self.a = a
        self.b = b

    # def printValues():
    #     print(a)
    #     print(b)

obj = Hello("Hello",2)
print(obj.a)
print(obj.b)
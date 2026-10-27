class A:
    def methodA(self):
        print("Class 1")

class B(A):
    def methodB(self):
        print("Class 2")

class C(A):
    def methodC(self):
        print("Class 3")

class D(B, C):
    def methodD(self):
        print("Class 4")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()
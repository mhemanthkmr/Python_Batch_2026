# add_two_number # Snake Case
# MathCalulatorTest # Pascal Case

class MathCalc:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)

obj1 = MathCalc(10,12) # 22
obj2 = MathCalc(100,200) # 300
obj3 = MathCalc(1000,2000) # 3000

obj1.add()
obj2.add()
obj3.add()

obj1.mul()
obj2.mul()
obj3.mul()

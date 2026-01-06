class MathCalc:

    def __init__(self, x, y): # Constructor
        self.x = x
        self.y = y

    def add(self):
        try:
            z = self.x + self.y
            return z
        except Exception:
            print("Something went wrong")
    
    def sub(self):
        try:
            z = self.x - self.y
            return z
        except Exception:
            print("Something went wrong")

    def div(self):
        try:
            z = self.x / self.y
            return z
        except Exception:
            print("Something went wrong")

    def mul(self):
        try:
            z = self.x * self.y
            return z
        except Exception:
            print("Something went wrong")

    def report(self):
        print("The Value of A: ",self.x)
        print("The Value of A: ",self.y)
        print("The addition of A and B", self.add())
        print("The subtraction of A and B", self.sub())
        print("The multiplication of A and B", self.mul())
        print("The division of A and B", self.div())
        print("========== END OF REPORT ==========\n\n")
    
    def export_report_as_text_file(self):
        try:
            data = f"""The Value of A: ",{self.x}
The Value of A: ",{self.y}
The addition of A and B", {self.add()}
The subtraction of A and B", {self.sub()}
The multiplication of A and B", {self.mul()}
The division of A and B", {self.div()}
========== END OF REPORT ==========\n\n"""
            file_name = f"report_{self.x}_{self.y}.txt"
            with open(file_name, mode="w") as file:
                file.write(data)
            print(f"Report Saved Successfully in {file_name}")
        except:
            print("Something went wrong")

# obj1 = MathCalc(30,40)
# obj1.report()
# obj1.export_report_as_text_file()
# obj2 = MathCalc(100,200)
# obj2.report()
# obj2.export_report_as_text_file()



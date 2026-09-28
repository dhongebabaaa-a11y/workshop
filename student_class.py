class Student:
    def __init__(self,name):
        self.name=name
    def greet(self):
       return f"Hi , I am {self.name}"

s1=Student("Anita")
print(s1.greet())
       
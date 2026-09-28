class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        if self.marks>=40:
          return f"{self.name} pass"
        else:
            return f"{self.name} fail"
        


s1=Student("ramu_vai",80)
s2=Student("hari_kaka",20)
s3=Student("dogesh",98)

print(s1.result())
print(s2.result())
print(s3.result())
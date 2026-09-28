class Fruits:
    def __init__(self,name):
       self.name=name
    def describe(self):
       return f"This fruit is called {self.name}"
 
f1=Fruits("Apple")
f2=Fruits("Banana")

print(f1.describe())
print(f2.describe())
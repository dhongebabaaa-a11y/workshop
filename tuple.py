fruits=( "apple","banana","watermelon")
single=(1,) #comma required for single item
mixed= ("pams",33,"helper")
print(fruits[0],fruits[-1])
print(fruits[0:2])
name,age,role=mixed
nums=(4,5,3,6,2)
combined=fruits + ("grapes",)
print("Total Items:", len(combined))
nested = ("point", (3,4))
print("x:",nested[1][0])


# a=quantity , b=minutes per garment , c=workers , d=efficiency
def calculate_productive_time(a,b,c,d):
 total_work_minutes=(a*b)
 theoretical_minutes=total_work_minutes / c
 actual_minutes=theoretical_minutes / (d / 100)
 hours=actual_minutes /60
 return hours

print("GARMENTS PRODUCT TIME PRIDICTOR")
a=int(input("Quantity: "))
b=float(input("minutes per garment: "))
c=int(input("Workers: "))
d=float(input("Efficiency: "))

calculated_hrs=calculate_productive_time(a,b,c,d)
print(f"\n Estimated Production time: {calculated_hrs:.2f} hrs")
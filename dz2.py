import random

print("Task 1")
a=int(input("Select number 1 or 0:"))
if a==1:
	print("0")
elif a==0:
	print("1")
else:
	print("error")


print("Task 2")
a=float(input("Enter your number:"))
b=float(input("Enter your number:"))
c=float(input("Enter your number:"))
print("Sum:", a+b+c)
print("Multiplication:", a*b*c)
print("geometric mean", round((a*b*c)**(1/3),2))

print("Task 3")
a=int(input("d1:"))
b=int(input("d2:"))
print("S=(d1*d2)/2=", (a*b)/2)

print("Task 4")
a=float(input(" °C:"))
print("°F:", (a*9/5)+32)

print("Task 5")
a=random.randint(1,10)
b=random.randint(11,99)
c=random.randint(1,100)
d=(((a**2+b**2)**(1/2))/c)*((a*b*c)/(a+b+c))
print(a,b,c)
print(round(d,2))

print("Task 6")
a=int(input("enter a:"))
b=int(input("enter b:"))
c=random.randint(10,1000)
print(c)
print(a<c<b)

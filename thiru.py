
                                      #python list
a={1,2,3}
for i in a:
    print(i)
print(2 in a)    
python set methods:
#add():
my_set={1,2,3}
my_set.add(3)
print(my_set)
#update():
my_set={1,2,3}
my_set.update([2,3,4])
print(my_set)
#discard
my_set={1,2,3}
my_set.discard(2)
print(my_set)
#remove
my_set={1,2,3}
my_set.discard(3)
print(my_set)
#pop
my_set={1,2,3}
my_set.pop()
print(my_set)
#clear
my_set={1,2,3}
my_set.clear()
print(my_set)
                                             #python tuple
#tuple
tup=(1."hi",2.5)
#tuple indexing
tup=(1,2,3,4,5,6)
print(tup[0])



#neagitive indexing
tup=(1,2,3,4,5,6)
print(tup[-1])
#tuple slicing
tup=(1,2,3,4,5,6)
print(tup[0:3])
# lst extend()
l=["hello,world","python","programming"]    
l2=["hi","java","coding"]
l.extend(l2)
print(l)
#dictionary
d={"name":"ramu","age":80}
d["age"]=30
print(d)
#create a function
def hello():
    print("hello, world!")
    # call a functin
hello()
print("end of the program")   
#arguments
def add(num1,num2):
    sum=num1+num2
    print("sum",sum)
add(5,6)
print("end of the program")    
#leap year
def is_leap(year):
    leap = False
    if year%400 == 0:
       leap = True
    elif year%100 == 0:
        leap = False
    elif year%4 == 0:
        leap = True    
    
    return leap

year = int(input())
print(is_leap(year))


  problems
#personal details
name = "John"
age = 25
city = "Thanjavur"

print("Name:", name)
print("Age:", age)
print("City:", city)
#user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print("name:", name)
print("age:", age)
print("city:", city)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#area of circle
radius = float(input("Enter radius: "))

pi = 3.14159
area = pi * radius * radius

print("Area of circle:", area)

#swaping two values without temp variaple
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, ", b =", b)

a, b = b, a

print("After swapping: a =", a, ", b =", b)
#swaping two values with temp variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)
#area of triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height

print("Area of triangle:", area)
#area of circle
adius = float(input("Enter radius: "))
area = 3.14 * radius ** 2

print("Area of circle:", area)
#area od rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)

print("Perimeter of rectangle:", perimeter)
#Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
#Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius:", celsius)
#Simple Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
#Compound Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

compound_interest = principal * (1 + rate/100) ** time - principal

print("Compound Interest:", compound_interest))
#Average of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average:", average)










    




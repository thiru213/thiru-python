n = int(input("Enter a number: "))
sum = 0
temp = n
while n > 0:
    digit = n % 10
    fact = 1 
    
    for i in range(1, digit + 1):
        fact = fact * i
    sum = sum + fact
    n = n// 10
if sum == temp:
    print( "is a strong number")
else:
    print( "is not a strong number")


    






 




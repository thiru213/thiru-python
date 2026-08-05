n = int(input("Enter a number: "))
square = n * n
temp = square
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10
if sum  == n:
    print( "is a neon  number")
else:
    print( "is not a neon number")


    






 




n = int(input("Enter a number: "))
sum = 0
temp = n
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n// 10
if temp % sum  == 0:
    print( "is a harshad number")
else:
    print( "is not a harshad number")


    






 




n = int(input(" enter a number:"))
temp = n
digit = len(str(n))
total = 0
while temp > 0:
    d = temp % 10
    total =  total + d * d * d 
    temp = temp // 10
if total == n:
    print("the number is armstrong")
else:
    print("the number is not armstrong")



    



    






 




n =  int(input("enter a n value"))
count = 0
while n >0:
    digit = n % 10
    if digit % 2 != 0:
      count = count + 1
    n = n // 10
print("odd digits:",count)

    






 




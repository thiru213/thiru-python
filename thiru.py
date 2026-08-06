x = 80
y = 60

g = 1

for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        g = i

lcm = (x * y) // g

print(lcm)







 




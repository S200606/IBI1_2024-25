a = 15
b = 75 #75minutes=1hour15minutes
c = a + b
d = 90
e = 5
f = d + e
#taking a bus takes more time than driving, driving is quicker
if c > f:
    print("taking a bus takes more time than driving")
elif c == f:
    print("taking a bus takes the same time as driving")
else:
    print("taking a bus takes less time than driving")



X = True
Y = False
W = X and Y
print("W的值是 ", W)
# W的真值表：
# X | Y | W (X and Y)
# ---------------
# T | T | T
# T | F | F
# F | T | F
# F | F | F

      
    
    
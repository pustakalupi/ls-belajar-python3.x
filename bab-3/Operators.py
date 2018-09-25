'''
done
'''
x = 8
y = 16

#arithmetic
print("arithmetic")
print(x + y) #24
print(x - y) #-8
print(x * y) #128
print(x / y) #0.5
print(x % y) #modulo
print(x ** y) #pangkat
print(x // y) #floor division
print("==============")
print("==============")

#comparison
print("comparison")
print(x == y) #False
print(x != y) #True
print(x > y) #False
print(x < y) #True
print(x >= y) #False
print(x <= y) #True
print("==============")
print("==============")

#assignment
print("assignment")
z = x + y
print(z)
z += x
print(z)
z -= y
print(z)
z *= x
print(z)
z /= x
print(z)
z %= x
print(z)
z **= x
print(z)
z //= x
print(z)
print("==============")
print("==============")

#bitwise
print("bitwise")
print(x & y) #AND
print(x | y) #OR
print(x ^ y) #XOR
print(x >> y) #right shift
print(x << y) #left shift
print(~x)
print("==============")
print("==============")

#logical
print("logical")
print((True and False)) #False
print((True or False)) #True
print(not (True and False)) #True
print("==============")
print("==============")

#membership
print("membership")
z = {1, 8, 9}
print(x in z) #True
print(y in z) #False
print(x not in z) #False
print("==============")
print("==============")
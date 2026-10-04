# 1. Arithmetic operators
print (10+8) #18
print (10-8) #2
print (10*8) #80
# /always give float value
print (10/8) #1.25
print (10//8) #1
print (10%8) #2
print (10**8) #100000000

# 2. Comparison Operators
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(3 <= 5)   # True

# 3. Assignment Operators

x = 10          # Simple assignment
x += 5          # 15
x -= 3          # 12
x *= 2          # 24
x /= 4          # 6.0
x //= 2         # 3.0
x %= 2          # 1.0
x **= 3         # 1.0
print(x)         # 1.0

# 4. Logical Operators
# AND
print(True and False)  #  False
# OR
print(True or False)   #  True
# NOT
print(not True)        #  False

# 5. Bitwise Operators
print(5 & 3)    # 1 
print(5 | 3)    # 7 
print(5 ^ 3)    # 6 
print(~5)       # -6 
print(5 << 1)   # 10 
print(5 >> 1)   # 2

# 6. Membership Operators
print("a" in "apple")      # True
print("z" not in "apple")  # True
print("A" in "apple")      # False

# 7. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)      # True 
print(a is c)      # False 
print(a is not c)  # True
print(id(a))
print(id(b))
print(id(c))

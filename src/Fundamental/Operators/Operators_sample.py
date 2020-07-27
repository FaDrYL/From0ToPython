"""
Author: FaDr_YL (_YL_)
"""


print("\n--- Arithmetic Operators ---\n")

x = 10
y = 3
print("x = {}; y = {}".format(x, y))
print("x + y = " + str(x + y))
print("x - y = " + str(x - y))
print("x * y = " + str(x * y))
print("x / y = " + str(x / y))
print("x % y = " + str(x % y))
print("x // y = " + str(x // y))
print("x ** y = " + str(x ** y))

print("\n--- Assignment Operators ---\n")

x = 1
print("Before: x = " + str(x))
print("x += 1")
x += 1
print("After: x = " + str(x))

print("\n--- Bitwise Operators ---\n")

a = 1
b = 7
print("a = {}; b = {}".format(a, b))
print("a & b = " + str(a & b))
print("a | b = " + str(a | b))
print("a ^ b = " + str(a ^ b))
print("~a = " + str(~a))
print("b << 2 = " + str(b << 2))
print("b >> 2 = " + str(b >> 2))

print("\n--- Comparison Operators ---\n")

a = 5
b = 8
print("a == b ? " + str(a == b))
print("a != b ? " + str(a != b))
print("a > b ? " + str(a > b))
print("a < b ? " + str(a < b))
print("a >= b ? " + str(a >= b))
print("a <= b ? " + str(a <= b))

print("\n--- Identity Operators ---\n")

a = 1
b = a
print("a is b ? " + str(a is b))
print("a is not b ? " + str(a is not b))

print("\n--- Logical Operators ---\n")

a = 2
print("a > 0 and a < 3 ? " + str(a > 0 and a < 3))
print("a < 0 or a > 3 ? " + str(a < 0 or a > 3))
print("not a > 0 ? " + str(not a > 0))

print("\n--- Membership Operators ---\n")

print("\"o\" in \"book\" ? " + str("o" in "book"))
print("1 not in [2, 3, 4] ? " + str(1 not in [2, 3, 4]))

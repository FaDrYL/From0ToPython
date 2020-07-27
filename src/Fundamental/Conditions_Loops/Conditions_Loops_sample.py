"""
Author: FaDr_YL (_YL_)
"""


x = 5

print("----- First If -----")
if x > 0:                       # True
    print("x is greateter than 0.")
print("end of first if")


print("----- Second If -----")
if x == 0 or x == 1:            # False
    print("x is 0 or 1")
print("end of second if")

print("----- If-Else -----")
if x < 0:
    print("x is a negative number.")
else:
    print("x is not a negative number.")


print("----- If-Elif-Else -----")
if x > 10:
    print("x is greater than 10.")  # not met
elif x > 5:
    pass   # not met
elif x == 5:
    print("x is 5.")                # met
elif x > 0:
    print("x is greater than 0.")   # ignore
else:
    print("all conditions are not met.")    # ignore
print("end of if-statement.")


print("----- Nested If -----")
if x > 0:
    print("x is greater than 0.")

    if x > 10:
        print("x is greater than 10.")
    else:
        print("x is not greater than 10.")

else:
    print("x is not greater than 0.")


print("----- Short If -----")
print("x is 5.") if x == 5 else print("x is not 5")


print("----- For Loop -----")
for i in range(0, 5):
    print(i)


print("----- For Loop With Else -----")
a_list = ["for", "while"]
for i in range(len(a_list)):
    print(i, a_list[i])
else:
    print("finished!")


print("----- From 1 add to 100 -----")
count = 1
the_sum = 0

while count <= 100:
    the_sum += count
    count += 1

print("sum: " + str(the_sum))

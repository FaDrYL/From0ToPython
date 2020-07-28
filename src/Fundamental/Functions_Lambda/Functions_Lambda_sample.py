"""
Author: FaDr_YL (_YL_)
"""


def a_function():
    # This is a function and does nothing.
    pass


def print_sub(a, b):
    print("print_sum is running")
    the_sum = a - b
    print(str(the_sum))


def calc_sum(a, b=0, c=0):
    return a + b + c


def func_many(*nums):
    for i in nums:
        print(i)


def func_many_kw(**kwargs):
    print("kwargs: " + str(kwargs))
    print("main num: " + str(kwargs["main_num"]))


def change_int(a):
    a = 10      # this a becomes a new object.
    print("In function: " + str(a))


def change_list(a):
    a.append(5)     # modify the original object.
    print("In function: " + str(a))


# From "num" add to 0
def recursion_sum(num):
    # check the base case
    if num <= 0:
        return 0

    # do some process
    return num + recursion_sum(num-1)


# this part will be executed, only if run this file directly.
if __name__ == "__main__":
    a_function()

    print("\n-----\n")

    print_sub(10, 5)
    print_sub(a=2, b=1)

    print("\n-----\n")

    print(calc_sum(10))
    print(calc_sum(8, c=2))
    print(calc_sum(5, 2, 3))

    print("\n-----\n")

    func_many(1, 2, 3, 4)

    print("\n-----\n")

    func_many_kw(num_one=10, main_num=20)

    print("\n-----\n")

    a_int = 0
    print("Before: " + str(a_int))
    change_int(a_int)
    print("After: " + str(a_int))

    print("\n-----\n")

    a_list = [1, 2]
    print("Before: " + str(a_list))
    change_list(a_list)
    print("After: " + str(a_list))

    print("\n-----\n")

    sum_100 = recursion_sum(100)
    print("0 add to 100: " + str(sum_100))
    sum_50 = recursion_sum(50)
    print("0 add to 50: " + str(sum_50))



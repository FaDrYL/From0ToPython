"""
Author: FaDr_YL (_YL_)
"""


def binary_func(x):
    # condition
    if x != 1 and x != 0:
        raise ValueError("x can only be 0 or 1.")
    pass


if __name__ == "__main__":
    # loop until the input is correct.
    while True:
        try:
            in_string = input("Enter a number: ")
            # error if in_string is not a number.
            in_int = int(in_string)
            # error if in_int is not match the condition in binary_func()
            binary_func(in_int)
        except ValueError as ex:
            print("Has error")
            print(ex)
        else:
            print("No error")
            break


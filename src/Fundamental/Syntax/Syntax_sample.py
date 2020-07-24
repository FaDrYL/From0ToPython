"""
Author: FaDr_YL (_YL_)
"""


import keyword

# Keyword list
print(keyword.kwlist)

print("-----")

print("Before the comment.")    # Single-line comment.
"""
multi-lines comments
second line.
"""
print("After the comment.")

print("-----")

x = 5
if x > 0:
    # 4-spaces indentation.
    print("x is a positive number.")

print("-----")

the_sentence = "first line." + \
               "second line." + \
               "third line."
print(the_sentence)

the_sentence_2 = """first line.
                 second line.
                 third line."""
print(the_sentence_2)

print("-----")

item_list = ["itemOne", "itemTwo", "itemThree",
           "itemFour", "itemFive"]
print(item_list)

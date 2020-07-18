# Variables & Data Types
![https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/) 

**Variable** is used to store data.

**Data Type** is the type of variable.



## Variables
In Python, you can create variables without declare the type.

A variable is created once you assigned a value to it.



### Variable name

There are some rules for variables name:

- Variable name can only **start** with *letter* or *underscore*:
  - variable_name
  - \_variableName
  - variable2
  - variable3\_
- Variables name are **case-sensitive**:
  - `variableName` and `variablename` are different variables.



Conventions:

- Easy to read:
  - variableName
  - variable_name
- Better be descriptive:
  - x_axis
  - website_link


Two kind of variables:
- Global variables
  - created on the outside of function. (we will see "function" later)
- Local variables
  - created on the inside of function.



### Assign value

Equal sign `=` is used for value assignment.

- Left side of `=`: the variable name.
- Right side of `=`: the value to assign.

Such as:

```Python
#  Name   |    Value
item_name = "the item"   # string
item_price = 9.95        # number (float)
item_stock = 10          # number (int)
```



#### Multi-values Assignment
##### 1 to Many
Python allowed that assign one value to multiple variables.

All variables `var_one`, `var_two` and `var_three` are `0` in this case:

```Python
var_one = var_two = var_three = 0
```



##### Many to Many
You can assign multiple values to multiple variables in one statement.

Using comma `,` to separate them:

```Python
var_one, var_two, var_three = 1, 2, "3rd variable"

print(var_one)
print(var_two)
print(var_three)
```

Run the code above will get the output:

```
1
2
3rd variable
```



## Data Types
Python has some principal built-in data types:
- [Number](#number)
- [Boolean](#boolean)
- [String](#string)
- [Tuple](#tuple)
- [List](#list)
- [Set](#set)
- [Dictionary](#dictionary)



Immutable data: Number, Boolean, String, Tuple.

Mutable data: List, Set, Dictionary.



> We can use `type()` method to check the exact data type of variable.
> ```Python
> >>> x = 1
> >>> print(type(x))
> <class 'int'>
> ```
> `



### Number
Python have `int`, `float`, and `complex` classes for number. ("Class" will be covered later)

```Python
>>> a_int, a_float, a_complex, second_complex = 100, 5.2, 1+3j, complex(2, 1)
>>> print(type(a_int))
<class 'int'>
>>> print(type(a_float))
<class 'float'>
>>> print(type(a_complex))
<class 'complex'>
>>> print(type(second_complex))
<class 'complex'>
```

> `del` can be used to delete an object (a variable by now). ("Object" will be covered latter)  
> single object: `del var_one`  
> multiple objects: `del a_int, a_float`



### Boolean
the class for boolean is `bool`.

Two keywords:
- True
- False

```Python
>>> isEnd = False
>>> print(type(isEnd))
<class 'bool'>
>>> print(isEnd)
False
```



### String
the class for string is `str`.
String is wrapped by either `"` or `'`.

```Python
>>> a_string = "String one"
>>> single_quote_string = 'String two'
>>> print(type(a_string))
<class 'str'>
>>> print(type(single_quote_string))
<class 'str'>
```



#### Escape Character
We need using escape character for some character which is not legal in a string.

Escape character can be used as a backslash `\ ` and follow by the character.

```Python
>>> a_string = "\"string\" with quotation mark."
>>> print(a_strig)
"string" with quotation mark.
```

Escape sequence table from [https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals):

| Escape Sequence | Meaning                        | Notes |
|-----------------|--------------------------------|-------|
| \newline        | Backslash and newline ignored  |       |
| \\              | Backslash (\)                  |       |
| \'              | Single quote (')               |       |
| \"              | Double quote (")               |       |
| \a              | ASCII Bell (BEL)               |       |
| \b              | ASCII Backspace (BS)           |       |
| \f              | ASCII Formfeed (FF)            |       |
| \n              | ASCII Linefeed (LF) (New line) |       |
| \r              | ASCII Carriage Return (CR)     |       |
| \t              | ASCII Horizontal Tab (TAB)     |       |
| \v              | ASCII Vertical Tab (VT)        |       |
| \ooo            | Character with octal value ooo | (1,3) |
| \xhh            | Character with hex value hh    | (2,3) |



#### String Slicing
String is an array of unicode characters (In Python, a character is a string with the length of 1).

So, you can get a character by using square bracket `[]` with an index number, after the string.

Index is start with `0`.

Also, negative number can represent an index from the end, last one is `-1`. 

```Python
a_string = "this is a string"
first_char = a_string[0]
last_char = a_string[-1]
print("first char is \'" + first_char + "\', last char is \'" + last_char + "\'.")
```

output:

```
first char is 't', last char is 'g'.
```



##### Slicing
Using `[]` with start index (inclusive), end index (exclusive), and separated by a colon `:` to get a part of string.

```Python
a_string = "Hello, world!"
first_word = a_string[0:5]          # or a_string[:5]
remaining_part = a_string[5:]       # or a_string[:len(a_string)]
print("length of a_string: " + len(a_string))
print("first part: " + first_word)
print("remaining part: " + left_part)
```

output:

```
length of a_string: 13
first part: Hello
remaining part: , world!
```



#### String Methods
Some string built-in methods:

Using them like `a_string.capitalize()`.

Parameters with `=` can be ignored, like `string.endswith(".txt")` rather than `string.endswith(".txt", 0, len(str))`

| Method | Description |
|:-------|:------------|
| capitalize() | Converts the first letter to upper case |
| center(width, fillchar) | Return Centered string with length of *width* and fill up the start and end by *fillchar* |
| encode(encoding="UTF-8", errors="strict") | Return encoded string |
| endswith(suffix, beg=0, end=len(string)) | Return True if the string end with *suffix*. If *beg* and *end* have values, it will only check this range. |
| expandtabs(tabsize=8) | Changes the tab to spaces with length of *tabsize* (by default, 8) |
| find(str, beg=0, end=len(string)) | Return the index of *str* if it is found in range *beg* to *end*, otherwise return `-1` |
| format(str1, str2 ...) | Return formatted string with values (*str1*, *str2*, ...) |
| index(str, beg=0, end=len(string)) | Same as find(str). But it will throw an exception if it is not found |
| isalnum() | Return True if all characters in the string are in the alphabet or digits. |
| isalpha() | Return True if all characters in the string are in the alphabet |
| isdecimal() | Return True if all characters in the string are decimals (include unicode characters which are numbers, like square) |
| isdigit() | Return True if all characters in the string are digits |
| isidentifier() | Return True if the string is a valid identifier |
| islower() | Return True if all characters in the string are lower case |
| isnumeric() | Return True if all characters in the string are numeric (include numeric in Chinese, like "五") |
| isprintable() | Return True if all characters in the string are printable |
| isspace() | Return True if all characters in the string are whitespaces |
| istitle() | Return True if the string follows the rules of a title (all words in string are started with a upper case latter, and rest of letters are lower case) |
| isupper() | Return True if all characters in the string are upper case |
| join(iterable) | Joins the elements of an *iterable* to the end of the string |
| ljust(width, fillchar=" ") | Left align the string and using fillchar to fill the rest part |
| lower() | Return lower case version of the string |
| lstrip(char=" ") | Removes leading *char* |
| maketrans(intab, outtab) | Return a translation table (letter in *intab* becomes letter in *outtab* with corresponding position) |
| partition(pivot) | Return a tuple which has 3 items. It will divide the string to 3 parts by *pivot* ("abcd".partition("b") -> ("a", "b", "cd")). |
| replace(old, new, max=null) | Return a string where *old* is replaced with *new*, and only for *max* times (by default, all *old* will be replaced) |
| rfind(...) | Same as find(), but start from right |
| rindex(...) | Same as index(), but start from right |
| rjust(...) | Same as ljust(), but start from right |
| rpartition(...) | Right version of partition() |
| rsplit(...) | Right version of split() |
| rstrip(...) | Right version of strip() |
| split(str="", num=string.count(str)) | Split the string to list. using *str* as separator, and split *num* times (by default, split each characters as an item to list) |
| splitlines(keepends=False) | Splits a string into a list by line breaks. keepends: keep the line breaks? (by default, it will remove all line breaks) |
| startswith(prefix, beg=0, end=len(string)) | Return True if the string start with *prefix* in range from *beg* to *end* |
| strip(char="") | Combination of lstrip(char) and rstrip(char) |
| swapcase() | Swap upper case to lower case and in other way round |
| title() | Converts the first character of each word to upper case |
| translate(trans_table, delete="") | Return a translated string which is translated by *trans_table* and remove characters in *delete* |
| upper() | Return upper case version of the string |
| zfill(width) | Right align the string and fill the left by `0` |

[Learn more](https://docs.python.org/3/library/stdtypes.html#string-methods)



### Tuple
Tuple **cannot** be **modified** after be created.
- unchangeable (immutable)

Items are be wrapped by `()` and separated by `,`.

```Python
a_tuple = ("item_1", "item_2")
diff_type_tuple = ("item_1", 100, 1.2)
```



#### Tuple Item Accessing
Tuple can be sliced and item can be got by an index. Same as [String](#string-slicing)

```Python
a_tuple = ("item_1", "item_2", "3", "4", "5")
print(a_tuple[0])
print(a_tuple[-2])
print(a_tuple[2:4])
```

output:

```
item_1
4
("3", "4")
```



> we cannot use `del item` to delete an item in a Tuple.



#### Special Cases For Creation
Tuple with 0 item: `tuple_0 = ()`

Tuple with 1 item: `tuple_1 = (100, )`

> Don't forget the comma `,`!



### List
List is an important data type.

We can change it after it is created.
- Changeable (mutable)

It can be accessed by an index.
- Ordered Collection

Items is wrapped by `[]` and separated by `,`.

```Python
a_list = [1, 2, 3, 4, 5]
diff_type_list = [0, "1", 2.0, True]
express_list = [x for x in range(3)]        # [0, 1, 2]
```



#### List Item Accessing And Changing
Same as [Tuple](#tuple-item-accessing) and [String](#string-slicing), item can be got by an index and slicing

**Get Item and Slicing**
```Python
>>> a_list = [0, 1, 2, 3, 4, 5]
>>> print(a_list[0])
0
>>> print(a_list[-3])
3
>>> print(a_list[1:4])
[1, 2, 3]
>>> print(a_list[::2])    # The third parameter is step size.
[0, 2, 4]
```



**Change Item**: assign a new value to the position in list.
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list[1] = 100
>>> print(a_list)
[0, 100, 2, 3]
```



**Add Item**:
- `append(item)`, append item to the last.
- `insert(index, item)`, insert item to a certain position.
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list.append(4)
>>> print(a_list)
[0, 1, 2, 3, 4]
>>> a_list.insert(0, -1)
>>> print(a_list)
[-1, 0, 1, 2, 3, 4]
```



**Remove Item**
- `remove(item)`, remove a specific item.
- `del list[index]`, remove a specific item.
- `pop(index=len(list))`, pop the item at the specified index (by default, last one).
- `clear()`, clear all items.
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list.remove(2)
>>> print(a_list)
[0, 1, 3]
>>> a_list.pop()
>>> print(a_list)
[0, 1]
>>> del a_list[0]
>>> print(a_list)
[1]
>>> a_list.clear()
>>> print(a_list)
[]
```



**Swap items**
```Python
>>> a_list = [0, 1, 2, 3]
>>> a_list[0], a_list[2] = a_list[2], a_list[0]
>>> print(a_list)
[2, 1, 0, 3]
```



#### List Methods
There are some built-in methods: 

| Method | Description |
|:-------|:------------|
| append(item) | Adds *item* at the end of the list |
| clear() | Removes all the elements from the list |
| copy() | Returns a copy of the list |
| count(item) | Returns the count of elements which is *item* |
| extend(new_list) | Extends *new_list* to the end of the list. |
| index(item) | Returns the index of the first elements which is *item* |
| insert(index, item) | Insert an item to a certain index |
| pop(index=len(list)) | Removes the element at the specific index (by default, last one) |
| remove(item) | Removes the element which is *item* |
| reverse() | Reverses the order of the list |
| sort(reverse=False, key=myFunc) | Sorts the list |



### Set
Set is a list of elements (items) **without** duplicated elements.

It will automatically remove the duplicated elements.

Set can create with `{}` or `set(iterable)`. (Empty set must create as `set()`, not the `{}`)

```Python
>>> a_set = {'1', '2', '3', '4', '1', '2'}
>>> print(a_set)
{'1', '2', '3', '4'}
>>> a_set = set([1, 2, 3, 1])
>>> print(a_set)
{1, 2, 3}
```



### Dictionary
Dictionary is **unordered collection**.
Which means item cannot be accessed by an index. It is using the key instead.

Dictionary can create with `{}`, and is unordered collection of `key: value`.

**Key** is an identifier of an item. It should be unique and is immutable.

Using same key will update and overwrite the old value with new one.

```
>>> a_dict = {'name': "the_item", 'price': 9.95, 'stock': 10}       # create a dictionary
>>> print(a_dict[name])                 # access a item
the_item
>>> a_dict["desc"] = "just an item"     # add a new item
>>> a_dict['price'] = 8.5               # update a item
>>> print(a_dict)
{'name': "the_item", 'price': 8.5, 'stock': 10, 'desc': "just an item"}
>>> print(a_dict.keys())                # show all the keys
dict_keys(['name', 'price', 'stock', 'desc'])
>>> print(a_dict.values())              # show all the values
dict_values(['the_item', 8.5, 10, "just an item"])
>>> dict_2 = {x: x+2 for x in range(3)}
>>> print(dict_2)
{0: 2, 1: 3, 2: 4}
```



### Data Type Conversion
Convert `x` to different type:

| Function | Description |
|:---------|:------------|
| int(x) | Converts *x* to integer |
| float(x) | Converts *x* to float |
| complex(real, imag) | Create a complex number |
| str(x) | Converts *x* to string |
| repr(x) | Converts *x* to printable representation string |
| tuple(s) | Converts a sequence (iterable) *s* to tuple |
| list(s) | Converts a sequence (iterable) *s* to list |
| set(s) | Converts a sequence (iterable) *s* to set |
| dict(t) | Convert a `(key, value)` tuple *t* to dictionary |
| frozenset(s) | Convert a sequence (iterable) *s* to a unchangeable set |
| char(int) | Convert an integer *int* to a character |
| ord(char) | Convert a character *char* to an integer |
| hex(x) | Convert integer *x* to hex string (base 16) |
| oct(x) | Convert integer *x* to oct string (base 8) |




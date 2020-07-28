# Functions & Lambda
![From 0 To Python](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

<br/>

[[Code sample]](Functions_Lambda_sample.py)

<br/>

## Functions
A function is an organized block of code which will not run until you call it.

It can reduce the repetition of code use. You can define it and call (use) it in multiple times.

After it is done, it can return a result.

<br/>

### Creating Functions

Function block is started with `def` keyword, then function name and arguments in `()`.

argument list `()` can be empty:

```Python
def a_function():
    # This is a function and does nothing.
    pass
```

or has some arguments:

```Python
def print_sum(x, y):
    # This function will print (x + y).
    the_sum = x + y
    print(str(the_sum))
```

<br/>

### Calling Functions

You just need function name and arguments in `()` to call a function.

Functions must be defined before call them.

```Python
# define functions
def a_function():
    print("a_function is running")

def print_sum(x, y):
    print("print_sum is running")
    the_sum = x + y
    print(str(the_sum))

# call functions
a_function()

print_sum(1, 2)
```

output:

```
a_function is running
print_sum is running
3
```

<br/>

### Arguments

You can create a function with arguments or without it.

Different types of arguments:
- Mandatory Arguments (Positional)
- Keyword Arguments
- Default Arguments
- Arbitrary Arguments

<br/>

#### Positional Arguments

You must follow the position and number of arguments.

```Python
def func_minus(a, b):
    print(str(a - b))

func_minus(10, 2)   # -> 8
func_minus(2, 10)   # -> -8
```

<br/>

#### Keyword Arguments

Using keyword to specify the argument.

If combine keyword with positional, keyword must be placed after positional.

```Python
def func_division(dividend, divisor):
    print(str(dividend / divisor))

# positional
func_division(10, 2)        # -> 5

# 1 positional, 1 keyword  (positional must before keyword)
func_division(10, divisor=2)        # -> 5

# 2 keywords (in different order)
func_division(divisor=2, dividend=10)       # -> 5
```

<br/>

#### Default Arguments

You can set a default value for arguments.

the argument with default value can be ignored.

```Python
def func(a, b=0, c=0):
    print(str(a + b + c))

func(13)        # -> 13
func(12, 1)     # -> 13
func(10, 1, c=2)  # -> 13
```

<br/>

#### Arbitrary Arguments

If you don't know how many arguments will be passed, you can add a `*` before the argument.

```Python
def func(*nums):
    for i in nums:
        print(i)

func(1, 2, 3)
```

output:

```
1
2
3
```

<\n>

*or*

<\n>

Arbitrary keyword arguments (add `**` before the argument)

```Python
def a_func(**kwargs):
    print("main num: " + str(kwargs["main_num"]))

a_func(num_one=10, main_num=20)
```

output:

```
main num: 20
```

<br/>

### Passing Arguments

Two types of variables will get different result:
- Immutable
- Mutable

<br/>

#### Immutable Variable as Arguments

Change the immutable variable in function will not affect the original variable itself.

```Python
def change_int(a):
    a = 10      # this a becomes a new object.
    print("In function: " + str(a))

a_int = 0
print("Before: " + str(a_int))
change_int(a_int)
print("After: " + str(a_int))
```

output:

```
Before: 0
In function: 10
After: 0
```

<br/>

#### Mutable Variable as Arguments

Change the mutable variable in function will affect the passed one.

```Python
def change_list(a):
    a.append(5)     # modify the original object.
    print("In function: " + str(a))

a_list = [1, 2]
print("Before: " + str(a_list))
change_list(a_list)
print("After: " + str(a_list))
```

output:

```Python
Before: [1, 2]
In function: [1, 2, 5]
After: [1, 2, 5]
```

<br/>

### Return Values

Using `return` to return a value.

After `return` executed, it will jump back to caller.

```Python
def func_sum(a, b):
    return a + b

print(func_sum(10, 5))

a = 20
b = 10
c = func_sum(a, b)
print(c)
```

output:

```
15
30
```

<br/>

### Function Recursion

Function Recursion is the function call itself.

Recursion functions must have base case to return. Otherwise, it will not stop.

```Python
# From "num" add to 0
def recursion_sum(num):
    # check the base case
    if num <= 0:
        return 0

    # do some process
    return num + recursion_sum(num-1)

# in another recursion way
def recursion_sum_2(num, the_sum=0):
    # check the base case
    if num <= 0:
        return the_sum

    # do some process
    the_sum += num
    num -= 1
    return recursion_sum_2(num, the_sum)

# iteration version of it
def iteration_sum(num):
    the_sum = 0
    for i in range(num+1):
        the_sum += i
    return the_sum

print(recursion_sum(100))
print(recursion_sum_2(100))
print(iteration_sum(100))
```

output:

```
5050
5050
5050
```

<br/>

## Lambda
Lambda function is a small anonymous function (single statement).

You can have as many arguments as you want like the general function.
Also, you cannot use global variable in Lambda which only accept the argument as variable.

You can use it like a normal function call, and it will return the result.

**Syntax**: `lambda args : expression`

```
>>> add_sum = lambda x, y: x + y
>>> print(add_sum(10, 5))
15
```

<br/>

You can return a lambda function in normal function:

```
def the_func(multiplier):
    return lambda x: x * multiplier

times = the_func(10)    
# it is same as: times = lambda x: x * 10

print(times(2))

times_2 = the_func(5)
print(times_2(3))
```

output:

```
20
15
```


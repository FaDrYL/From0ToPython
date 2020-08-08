# 函数 & Lambda
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f)](https://www.fadryl.com/)

<br/>

[[代码示例]](Functions_Lambda_sample.py)

<br/>

## 函数
函数是一个组织好的代码块，这个代码块只会在你使用（调用）当前函数的时候才会运行。

它能减少项目中重复的代码，你能无限次的调用它。

函数运行完后，可以返回一个结果。

<br/>

### 创建（定义）函数

函数块以关键字 `def` 开头， 后面跟函数名以及在括号 `()` 内的参数（们）。

参数列表可以为空：

```Python
def a_function():
    # 这是个什么都不做的函数
    pass
```

或者有参数：

```Python
def print_sum(x, y):
    # 这个函数会输出 (x + y).
    the_sum = x + y
    print(str(the_sum))
```

<br/>

### 使用（调用）函数

直接使用 **函数名** 和 **相对应的参数** 来使用函数

函数必须先定义了才能使用它。

对于有参数的函数，使用它时必须传递对应的参数（传参）。

```Python
# 定义函数
def a_function():
    print("a_function is running")

def print_sum(x, y):
    print("print_sum is running")
    the_sum = x + y
    print(str(the_sum))

# 使用函数
a_function()

print_sum(1, 2)
```

输出:

```
a_function is running
print_sum is running
3
```

<br/>

### 参数

你可以定义一个有参数或者没参数的函数。

不同的参数类型:
- 位置参数 （必须参数）
- 关键字参数
- 默认参数
- 不定长参数

<br/>

#### 位置参数

你必须按照对应的位置和参数的数量来传递参数。

```Python
def func_minus(a, b):
    print(str(a - b))

#          a   b
func_minus(10, 2)   # -> 8
func_minus(2, 10)   # -> -8
```

<br/>

#### 关键字参数

使用关键字来指定对应的参数（对应名字，不用对应位置）。

如果与位置传参同时使用，关键字传参必须放在位置传参的后面。

```Python
def func_division(dividend, divisor):
    print(str(dividend / divisor))

# 位置传参
func_division(10, 2)        # -> 5

# 1 个位置传参, 1 个关键字传参  (位置传参要在关键字传参前)
func_division(10, divisor=2)        # -> 5

# 两个都是关键字传参 (可以不按顺序)
func_division(divisor=2, dividend=10)       # -> 5
```

<br/>

#### 默认参数

定义函数时，你可以设置参数的默认值。

有默认值的参数，在使用函数传参时可以忽略它

```Python
def func(a, b=0, c=0):
    print(str(a + b + c))

func(13)        # -> 13
func(12, 1)     # -> 13
func(10, 1, c=2)  # -> 13
```

<br/>

#### 不定长参数

如果你不确定有多少个参数会被传递，你可以加一个 `*` 在参数名前。

```Python
def func(*nums):
    for i in nums:
        print(i)

func(1, 2, 3)
```

输出:

```
1
2
3
```

<br/>

*或者*

<br/>

关键字不定长参数 （在参数名前加 `**`）

使用关键字来传递和访问参数。

```Python
def a_func(**kwargs):
    print("main num: " + str(kwargs["main_num"]))

a_func(num_one=10, main_num=20)
```

输出:

```
main num: 20
```

<br/>

### 传递参数（传参）

两个不同类型的变量传参会产生不同的结果：
- Immutable 不可变
- Mutable 可变

<br/>

#### 传递不可变类型

更改不可变变量（函数内）**不会**影响原本的变量（函数外）。

```Python
def change_int(a):
    a = 10      # a 变成了一个新的变量
    print("函数中: " + a)

a_int = 0
print("前: " + str(a_int))
change_int(a_int)
print("后: " + str(a_int))
```

输出:

```
前: 0
函数中: 10
后: 0
```

<br/>

#### 传递可变类型

改变可变变量（函数内）**会**影响原本的变量（函数外）。

```Python
def change_list(a):
    a.append(5)     # 改变原本的变量
    print("函数中: " + str(a))

a_list = [1, 2]
print("前: " + str(a_list))
change_list(a_list)
print("后: " + str(a_list))
```

输出:

```Python
前: [1, 2]
函数中: [1, 2, 5]
后: [1, 2, 5]
```

<br/>

### 返回结果

使用关键字 `return` 来返回一个结果。

当 `return` 执行后，函数就会结束，并返回到原本调用这个函数的地方。

```Python
def func_sum(a, b):
    return a + b

print(func_sum(10, 5))

a = 20
b = 10
c = func_sum(a, b)
print(c)
```

输出:

```
15
30
```

<br/>

### 递归函数

递归函数是一个函数，其自己调用自己。

递归函数必须有个最基本的情境来停止递归。不然，这个函数就不会停下了。

```Python
# 从 0 加到 num
def recursion_sum(num):
    # 检查最基本情境
    if num <= 0:
        return 0

    # do some process
    return num + recursion_sum(num-1)

# 另一种方式
def recursion_sum_2(num, the_sum=0):
    # 检查最基本情境
    if num <= 0:
        return the_sum

    # do some process
    the_sum += num
    num -= 1
    new_sum = recursion_sum_2(num, the_sum)
    return new_sum

# 迭代的版本
def iteration_sum(num):
    the_sum = 0
    for i in range(num+1):
        the_sum += i
    return the_sum

print(recursion_sum(100))
print(recursion_sum_2(100))
print(iteration_sum(100))
```

输出:

```
5050
5050
5050
```

<br/>

## Lambda
Lambda 函数是一个小的匿名函数 （单个语句）.

与普通的函数一样，你可以有多个参数。
另外，你不能在 Lambda 内使用全局变量，只能使用局部变量（参数）。

你可以像普通函数一样使用它，它会返回一个结果。

**语法**: `lambda args : expression`

```
>>> add_sum = lambda x, y: x + y
>>> print(add_sum(10, 5))
15
```

<br/>

你可以在普通函数中返回一个（可变的） lambda 函数：

```
def the_func(multiplier):
    return lambda x: x * multiplier

times = the_func(10)    
# it is same as: times = lambda x: x * 10

print(times(2))

times_2 = the_func(5)
print(times_2(3))
```

输出:

```
20
15
```


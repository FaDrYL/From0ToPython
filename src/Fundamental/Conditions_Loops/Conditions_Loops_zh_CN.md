# 条件判断 & 循环
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f)](https://www.fadryl.com/)

<br/>

[[代码示例]](Conditions_Loops_sample.py)

<br/>

## Conditions
**条件判断**

条件语句用于判断、决定需要执行的代码块。

流程图:

```
                如果是True
判断前 -----> 判断 -----> 判断语句内的代码块
              |                |
              |                |
              |如果是 False     |
              ------------------------------------------------> 判断后

```

<br/>

### If-statement
**if 语句**

关键字 `if` 用于开始 if 语句.

如果条件符合，条件内部的代码块将会执行。反之，这个代码块就会被忽略。（如果）

对于条件内的代码块来说，**缩进**很重要。
同时，它意味着这个代码块是属于当前 if 语句的。

```Python
x = 5

# 第一个 if 语句
if x > 0:                       # True
    print("x is greateter than 0.")    # 缩进!
print("end of first if")

# 第二个 if 语句
if x == 0 or x == 1:            # False
    print("x is 0 or 1")        # 这行代码会被忽略
print("end of second if")
```

输出:

```
x is greater than 0.
end of first if
end of second if
```

<br/>

#### Else

关键字 `else` 放置于 if 语句的末尾部分。

如果前面的条件都不符合，那么 `else` 内的代码块将会被执行。（不然）

```Python
x = 5

if x < 0:
    print("x is a negative number.")
else:
    print("x is not a negative number.")

print("end of if-else.")
```

输出:

```
x is not a negative number.
end of if-else.
```

<br/>

#### Else If

关键字 `elif` 放置于 if 语句的中间部分（`if` 后，`else` 前）。

同时，你可以使用随意数量的 `elif`。

只有第一个符合的条件之内的代码块将会被执行。之后就会跳出到整个 if 语句的外面。

```Python
x = 5

if x > 10:
    print("x is greater than 10.")  # 不符合
elif x > 5:
    print("x is greater than 5.")   # 不符合
elif x == 5:
    print("x is 5.")                # 符合，执行这行，完成后跳出 if
elif x > 0:
    print("x is greater than 0.")   # 忽略
else:
    print("all conditions are not met.")    # 忽略
print("end of if-statement.")
```

output:

```
x is 5.
end of if-statement.
```

<br/>

#### Nested If-statement
**嵌套 if 语句**

在 `if` 内的 `if`, 就被叫做嵌套 if 语句.

```Python
x = 5

if x > 0:
    print("x is greater than 0.")

    if x > 10:
        print("x is greater than 10.")
    else:
        print("x is not greater than 10.")

else:
    print("x is not greater than 0.")
```

输出:

```
x is greater than 0.
x is not greater than 10.
```

<br/>

#### Pass

if 语句内不能是空的，但是你可以用 pass 来替代留空。

```Python
x = 5

if x > 10:
    print("x is greater than 10.")
elif x == 5:
    pass
else:
    print("The else part.")

print("end of if-statement.")
```

输出:

```
end of if-statement.
```

<br/>

#### Conditional Expression
**条件语句表达式**

简单的 if-else 语句可以用一行完成。

```Python
x = 5

print("x is 5.") if x == 5 else print("x is not 5")

# 等同于:
if x == 5:
    print("x is 5.")
else:
    print("x is not 5.")

# 另一个例子：
a = 0
b = 10 if a == 0 else 20
print("b is " + str(b))        # 10
```

输出:

```
x is 5.
x is 5.
b is 10
```

<br/>

## Loops
**循环**

Python 有两种循环语句:
- `for` 循环
- `while` 循环

流程图:

```
               ----------------
               |              |
               v 如果是 True   |
判断前 ------> 判断 ------> 循环内的代码
               |
               |
               |如果是 False
               -------------------> 判断后
                   
```

<br/>

### For Loops
`for` 循环可以迭代所有在一个序列（iterable）中的元素。

```Python
for i in range(0, 5):
    print(i)

print("---")

for i in "for":
    print(i)

print("---")

a_list = ["for", "while"]
for i in range(len(a_list)):
    print(i, a_list[i])
else:
    print("finished!")      # 循环完成后
```

输出:

```
0
1
2
3
4
---
f
o
r
---
0 for
1 while
finished!
```

> 内置函数 `range(beg, end, step=1)` 可以创建一个数字序列.  
> `range(5)` -> `0 1 2 3 4`  
> `range(2, 5)` -> `2 3 4`  
> `range(0, 5, 2)` -> `0 2 4`  
> `range(5, 0, -1)` -> `5 4 3 2 1`

<br/>

### While Loops
`while` 循环使用条件语句来判断是应该继续循环，还是跳出循环。

`while` 语句的格式:

```Python
while <条件>:
    <代码>
```

和

```Python
while <条件>:
    <代码, 完成后跳回 while 进行判断>
else:
    <如果条件不符就运行这里的代码, 完成后跳出循环>
```

例子:

```Python
# 从 1 加到 100
count = 1
the_sum = 0

while count <= 100:
    the_sum += count
    count += 1

print("sum: " + str(the_sum))

print("---")

# 有 else 的例子
count = 1
the_sum = 0

while count <= 100:
    the_sum += count
    count += 1
else:
    print("while-loop is done and sum = " + str(the_sum))
```

输出:

```
sum: 5050
---
while-loop is done and sum = 5050
```

<br/>

### Break
使用关键字 `break` 来直接结束循环。

```Python
for i in range(10):
    print(i)
    
    # 如果 i = 3，就直接停止循环
    if i == 3:
        break
```

输出:

```
0
1
2
3
```

<br/>

### Continue
使用关键字 `continue` 来跳过当前循环剩下的代码，并直接进行下一个循环迭代。

```Python
for i in range(10):
    # 跳过所有单数
    if i % 2 == 1:
        continue
    
    print(i)
```

输出:

```
0
2
4
6
8
```

<br/>

## 还有一件事
到目前为止，你已经可以使用 Python 来做很多简单的事情了。

通过练习来掌握它吧。



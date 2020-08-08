# 输入 & 输出
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f)](https://www.fadryl.com/)

<br/>

这章会讲一些基础的 I/O 函数

<br/>

## 输出到屏幕
使用 `print()` 函数来将字符串输出到屏幕。

```Python
>>> print("Print")
Print
```

<br/>

使用 `.format(*args)` 和 `{}` 来格式化字符串。

```Python
>>> print("{0} and {1}.\n1: {1}, 0: {0}".format("First", "Second"))
First and Second.
1: Second, 0: First
```

<br/>

## 获取字符串输入
使用 `input(prompt="")` 来获取输入（字符串）。

`prompt` 为输入提示。

```Python
>>> x = input("enter a number for x? ")
enter a number for x? 10
>>> print(type(x))
<class 'str'>
>>> print(x)
10
```

<br/>

## 文件处理
使用 `open(filename, mode="rt")` 来打开文件以及进行处理。

！**不要忘记**关闭 `.close()` 打开了的文件。

文件处理有不同的模式：

| 模式 | 简述 |
|:---:|:---:|
| `r` | 读（默认）； 只用于读取文件，如果文件不存在就会报错 |
| `a` | 追加； 在文件末尾追加，如果文件不存在则创建文件 |
| `w` | 写； 将文件覆盖重写，如果文件不存在则创建文件 |
| `x` | 创建； 创建一个文件，如果文件已存在就会报错 |

<br/>

同时，你可以指定文件的类型。将其加至模式字母的后面：

| 类型 | 简述 |
|:---:|:---:|
| `t` | 文本（默认） |
| `b` | 二进制 |

<br/>

在模式的最后加 `+` 来读和写文件：

```Python
file = open(filename, mode="r+")    # 从开头写
file = open(filename, mode="w+")    # 从开头写，覆盖
file = open(filename, mode="a+")    # 从结尾写

file.close()
```

<br/>

### 读取文件内容
使用 `read(length)` 来读取文件内容。

*hello_world.txt*:

```
Hello, 
Python!
```

读取:

```Python
>>> file = open("hello_world.txt", "r")
>>> print(file.read())
Hello, 
Python!
>>> print(file.read(3))
Hel
>>> file.close()
```

另一种方式:

```Python
file_content = ""
file = open("hello_world.txt", "r")

for line in file:
    file_content += line

print(file_content)
# Hello,
# Python!

file.close()
```

<br/>

### 写入文件
使用 `write(...)` 来将字符串写入文件。

根据模式的不同，它会进行追加或覆盖。

```Python
file = open("hello_world.txt", "w")
file.write("Hello, world!")        # 覆盖
file.close()

file = open("hello_world.txt", "r")
print(file.read())
# Hello, world!
```



# 语法
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython)

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)](https://www.fadryl.com/)

<br/>

这章会讲 Python 的一些基本语法。

[代码示例](Syntax_sample.py)

<br/>

## Python 文件
Python 的文件后缀（文件拓展名）是 `.py`。

<br/>

## 关键字
我们**不能**以关键字命名*变量*和*函数*。

用以下方式来显示当前版本的所有关键字：

```python
$ python
>>> import keyword
>>> keyword.kwlist
```

它会显示所有关键字，比如：

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### 怎么退出？
直接输入来退出命令行中的 Python：

```
>>> quit()
```

<br/>

## 注释
注释用于备注、解释代码、代码文档，它不会被运行。

有两种注释类型：

1. 单行注释
2. 多行注释

<br/>

### 单行注释

单行注释以 `#` 开头。

```python
# 这是注释
print("Hello, world!")
```

以上代码运行后的输出：

```
Hello, world!
```

> `print()` 语句通常用于输出变量或字符串到屏幕上。

<br/>

### 多行注释

多行注释应该使用 `'''` 或 `"""` 来包裹住。

```python
'''
这是一个多行注释
第二行
'''

"""
这也是多行注释
第二行
"""

# 单行注释
```

<br/>

# 缩进
Python的最大特色是使用缩进来表示代码块，而不是使用花括号 `{}`。

通常是 `2个空格`, `4个空格` 或 `1个tab`。

```python
if 5 > 0:
    # 4个空格.
    print("5 是个正数")
```

<br/>

同一个代码块内应该使用一致的缩进方式。要不然，会报错 `IndentationError`。

<br/>

# 多行语句
一般来说，一个语句应该一行写完。

但是，如果它太长了，就可以使用反斜杠 `\` 来实现多行语句

e.g.

```python
theSentence = "写在第一行" + \
              "写在第二行" + \
              "写在第三行"
```

<br/>

在 `[]`, `{}`, `()` 中，我们可以不使用 `\` 来写多行注释。

比如：

```python
itemList = [itemOne, itemTwo, itemThree,
           itemFour, itemFive]
```

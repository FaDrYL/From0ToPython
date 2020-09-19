# Syntax
[![Project link](../../../res/badges_project.svg)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](../../../res/badges_github.svg)](https://github.com/FaDrYL)
[![Website link](../../../res/badges_website.svg)](https://www.fadryl.com/)

<br/>

There are some basic syntax for Python.

[[Code sample]](Syntax_sample.py)

<br/>

## Python File
Python files is ended with `.py`.

<br/>

## Keywords
We can **not** using keywords as variable name, method name and identifier.

Show all keywords of current Python version in command line by:

```python
$ python
>>> import keyword
>>> keyword.kwlist
```

It will show some keywords, for example:

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### How to quit?
Just enter:

```
>>> quit()
```

<br/>

## Comments
Comments is using for purpose of in-code documentation and will not be executed.

There are two types of comment:

1. Single-line comment.
2. Multi-lines comment.

<br/>

### Single-line Comment

Single-line comment start with `#` in Python.

```python
# that is a comment.
print("Hello, world!")
```

result after execute the code above:

```
Hello, world!
```

> `print()` statement is used to output variables or string to the screen. 

<br/>

### Multi-line Comment

Multi-lines comment is wrapped by `'''` and `"""`.

```python
'''
There is a multi-lines comments.
Second line.
'''

"""
There is also a multi-lines comments.
Second line.
"""

# single-line comment.
```

<br/>

# Indents
The most distinctive feature of Python is the use of indentation to represent code blocks, without the use of braces `{}`.

In general, it is `2 spaces`, `4 spaces` or a `tab`.

```python
if 5 > 0:
    # 4 spaces indentation.
    print("5 is a positive number")
```

<br/>

Indentations in one code blocks should be same. Otherwise, it will produce an error `IndentationError`.

<br/>

# Multi-line statement
In general, one statement should be done in one line.

But, if it is too long, we can use backslash `\` to implement a multi-line statement.

e.g.

```python
theSentence = "first line." + \
              "second line." + \
              "third line."
```

<br/>

In `[]`, `{}`, `()`, we can write multi-line statement without `\`.

e.g.

```python
itemList = [itemOne, itemTwo, itemThree,
           itemFour, itemFive]
```

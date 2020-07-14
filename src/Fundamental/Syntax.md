# Syntax
There are some basic syntax for Python.



## Keywords
We can **not** using keywords as variable name, method name and identifier.

Show all keywords of current python version in command line by:

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

Also, quit by `>>> quit()`.



## Comments
Comments is using for purpose of in-code documentation and will not be executed.

There are two types of comment:

1. Single-line comment.
2. Multi-lines comment.



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



### Multi-line Comment

Multi-lines comment is warped by `'''` and `"""`.

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



# Indents
The most distinctive feature of Python is the use of indentation to represent code blocks, without the use of braces `{}`.

In general, it is `2 spaces`, `4 spaces` or a `tab`.

```python
if 5 > 0:
    # 4 spaces indentation.
    print("5 is a positive number")
```


Indentations in one code blocks should be same. Otherwise, it will produce a error `IndentationError`.



# Multi-line statement
In general, one statement should be done in one line.

But, if it is too long, we can use backslash `\` to implement a multi-line statement.

e.g.

```python
theSentence = "first line." + \
              "second line." + \
              "third line."
```



In `[]`, `{}`, `()`, we can write multi-line statement without `\`.

e.g.

```python
itemList = [itemOne, itemTwo, itemThree,
           itemFour, itemFive]
```
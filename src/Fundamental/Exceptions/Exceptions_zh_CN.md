# 异常
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f)](https://www.fadryl.com/)

<br/>

当有错误发生时，就会抛出异常。

如果抛出的异常没有被接住（处理），程序就会停止运行。

你可以根据 bug 或错误进行**抛出**或者**处理**异常。

<br/>

## 抛出异常
使用 `raise <errorName>` 语句来将一个异常抛出。（[下面](#built-in-exceptions)列出了一些异常的名字）

```Python
def binary_func(x):
    if x != 1 and x != 0:
        # 抛出值异常（多用于参数的值不符合要求）
        raise ValueError("x can only be 0 or 1.")
    pass
```

当这个函数，使用 "2" 进行传参时：

```Python
Traceback (most recent call last):
  File "filePath", line 7, in <module>
    binary_func(2)
  File "filePath", line 3, in binary_func
    raise ValueError("x can only be 0 or 1.")
ValueError: x can only be 0 or 1.
```

<br/>

## 处理异常
使用 "try-catch" 语句进行异常的处理。

```Python
try:
    # 会先尝试运行这里的代码块。
    # 如果发生异常，则会忽略剩下的代码直接跳到 "except" 部分。
    ...
    # 如果没有异常，运行完成后则会跳到 "else" 部分（如果有的话）。
except <异常名>:
    # 如果没有 <异常名>, 则会接住所有的异常。
    # 如果抛出的异常于当前 <异常名> 符合，那么这个代码块将会被执行。
    ...
    # 执行完后，将忽略剩下所有的 "except" ，然后跳到 "finally" 部分（如果有的话）。
except <异常名>:
    # 如果上面的不匹配，将会检查这个。
    # "except" 部分不限制数量。
    ...
else:
    # [可选] 这里的代码会在 "try" 部分没有发生异常的情况下执行。
    ...
finally:
    # [可选] 这里的代码会在最后执行，有异常或无异常都会执行这里。
    ...

# 如果抛出的异常没有被接住（处理），它将会被再度抛出。
# 直到被接住，或者最后程序因异常停止。
```

例子:

```Python
def binary_func(x):
    if x != 1 and x != 0:
        raise ValueError("x can only be 0 or 1.")
    pass


while True:
    try:
        in_num = int(input("Enter a number: "))
        binary_func(in_num)
    except ValueError as ex:
        print(ex)
    else:
        break
```

<br/>

## 创建异常
你可以创建自定义的异常，只需继承至一个已存在的异常类：

```Python
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "From MyException:" + repr(self.msg)
```

<br/>

## Built-in Exceptions
内置的异常（常用）：

| Name | Description |
|:----:|:-----------:|
| `Exception` | The base class for all exceptions |
| `ArithmeticError` | Errors related to numeric calculation |
| `BufferError` | Errors related to buffer operation |
| `LookupError` | Base class for errors related to key or index |
| `AssertionError` | Raise when an assertion fail |
| `AttributeError` | Errors related to attribute reference or assignment |
| `EOFError` | Errors related to the `input()` reach end-of-file |
| `ImportError` | Errors related to `import` statement |
| `ModuleNotFoundError` | Errors related to `import` statement and the module not found |
| `IndexError` | Errors related to index of a sequence (e.g. List) |
| `KeyError` | Errors related to the key is not found in mapping structure (e.g. Dictionary) |
| `KeyboardInterrupt` | The program is interrupt by keyboard ("Control-C" or "Delete") during execution | 
| `MemoryError` | Errors related to run out of memory |
| `NameError` | Errors related to a name is not found |
| `NotImplementedError` | Errors for the functions is not be implemented (especially, related to abstract class) |
| `OSError` | Errors related to the system |
| `OverflowError` | Errors related to the result of an arithmetic operation is too large to be represented |
| `RecursionError` | Errors related to the recursion is exceeded the maximum recursion depth (sys.getrecursionlimit()) |
| `StopIteration` | For an iterator which has no more item to iterate |
| `SyntaxError` | Errors related to syntax |
| `TypeError` | Errors related to data type |
| `UnicodeError` | Errors related to decode and encode of unicode |
| `ValueError` | Errors related to the value of the argument is not correct (precondition) |
| `ZeroDivisionError` | Errors related to the second argument of a division or modulo operation is zero |
| `FileExistsError` | Errors related to a file is already exist |
| `FileNotFoundError` | Errors related to a file is not found |
| `PermissionError` | Errors related to the permission is denied |
| `TimeoutError` | Errors related to a system function timed out at the system level |

[点此了解更多内置的异常类](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)


# Exceptions
[![Project link](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB)](https://github.com/FaDrYL/From0ToPython)

[![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)](https://github.com/FaDrYL)
[![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)](https://www.fadryl.com/)

Exceptions will be throw when errors occur.

You can throw and handle exceptions to deal with bugs or mistakes.



## Throw Exceptions
Using `raise <errorName>` to throw an exception. (some errorName are listed [below](#built-in-exceptions))

```Python
def binary_func(x):
    if x != 1 and x != 0:
        raise ValueError("x can only be 0 or 1.")
    pass
```

if passing "2" to this function:

```Python
Traceback (most recent call last):
  File "filePath", line 7, in <module>
    binary_func(2)
  File "filePath", line 3, in binary_func
    raise ValueError("x can only be 0 or 1.")
ValueError: x can only be 0 or 1.
```



## Handle Exceptions
Using "try-catch" statement to handle exceptions.

```Python
try:
    # try this code block first. if has exception, will jump to "except" part directly.
    ...
    # no exception, jump to else.
except <exceptionName>:
    # if no <errorName>, 
    # if the exception match exceptionName, this code block will be executed.
    ...
    # after that, ignore remaining "except" and jump to "finally".
except <exceptionName>:
    # if the exception is not match above and this one is matched, this code block will be executed.
    # you can add as many "except" as you want.
    ...
else:
    # [Optional] this block will be run if no exception after "try" part.
    ...
finally:
    # [Optional] this block will be run after "else" or "except".
    # even has exception.
    ...

# if the exception is not be catched, it will be throw again.
```

Example:

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



## Create Customized Exception
You can create a customized exception by inherit an exception.

```Python
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "From MyException:" + repr(self.msg)
```



## Built-in Exceptions

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

[Find more](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)


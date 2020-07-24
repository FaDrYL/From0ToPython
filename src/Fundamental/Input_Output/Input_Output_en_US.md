# Input & Output
![https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

<br/>

This chapter will discuss some basic I/O functions.

<br/>

## Output To Screen
Using `print()` to print strings to screen.

```Python
>>> print("Print")
Print
```

<br/>

Using `.format(*args)` with `{}` in the string to format the output:

```Python
>>> print("{0} and {1}.\n1: {1}, 0: {0}".format("First", "Second"))
First and Second.
1: Second, 0: First
```

<br/>

## Get Input String
Using `input(prompt="")` to get the input (string).

```Python
>>> x = input("enter a number for x? ")
enter a number for x? 10
>>> print(type(x))
<class 'str'>
>>> print(x)
10
```

<br/>

## File Handling
Using `open(filename, mode="rt")` to work with files.

! Always don't forget to close `.close()` the opened file.

There has some different modes:

| Mode | Description |
|:----:|:-----------:|
| `r` | Read (default). Only for file reading, error if file does not exist. |
| `a` | Append. Append text to the file, create file if file does not exist. |
| `w` | Write. Overwrite the file, create file if file does not exist. |
| `x` | Create. Create the file, error if file exists |

<br/>

Also, you can specify the file type. Add it after the mode:

| Type | Description |
|:----:|:-----------:|
| `t` | Text (default) |
| `b` | Binary |

<br/>

Add `+` for read and write the file:

```Python
file = open(filename, mode="r+")    # from the beginning
file = open(filename, mode="w+")    # from the beginning, overwrite.
file = open(filename, mode="a+")    # from the end

file.close()
```

<br/>

### Read File
Using `read(length)` to read file.

*hello_world.txt*:

```
Hello, 
Python!
```

read file:

```Python
>>> file = open("hello_world.txt", "r")
>>> print(file.read())
Hello, 
Python!
>>> print(file.read(3))
Hel
>>> file.close()
```

Also, in another way:

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

### Write File
Using `write()` to write string to file.

According to the mode, it will append or overwrite.

```Python
file = open("hello_world.txt", "w")
f.write("Hello, world!")        # overwrite
file.close()

file = open("hello_world.txt", "r")
print(f.read())
# Hello, world!
```



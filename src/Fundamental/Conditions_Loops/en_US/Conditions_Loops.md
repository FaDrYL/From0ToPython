# Conditions & Loops
![https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB](https://img.shields.io/badge/From%200%20To-Python-blue?style=for-the-badge&logo=Python&logoColor=FFD43B&logoWidth=15&labelColor=566163&color=3776AB) 

![Github link](https://img.shields.io/badge/FaDrYL--blue?style=social&logo=Github&logoWidth=15&link=https://github.com/FaDrYL)
![Website link](https://img.shields.io/badge/FaDr-YL-blue?style=flat&color=009f9f&link=https://www.fadryl.com/&link=https://www.fadryl.com/)

<br/>

## Conditions
Conditional statement is used for determine which code block should execute.

Flow chart:

```
                        if is true
Before -----> Condition -----> Code block inside condition
                  |                        |
                  |                        |
                  |if is false             |
                  ------------------------------------------------> After

```

<br/>

### If-statement

Using `if` keyword for if-statement.

if the condition is met, the code inside this condition will be executed. Otherwise, ignore this block.

Indentation is important for code block inside the condition.
Also, it means the code block is belong to this if-statement.

```Python
x = 5

# First if-statement
if x > 0:                       # True
    print("x is greateter than 0.")    # Indent!
print("end of first if")

# Second if-statement
if x == 0 or x == 1:            # False
    print("x is 0 or 1")        # This line will be ignored
print("end of second if")
```

output:

```
x is greater than 0.
end of first if
end of second if
```

<br/>

#### Else

`else` keyword should be placed at the end of if-statement.

if all the conditions above are not met, the code block in the `else` will be executed.

```Python
x = 5

if x < 0:
    print("x is a negative number."
else:
    print("x is not a negative number.")

print("end of if-else.")
```

output:

```
x is not a negative number.
end of if-else.
```

<br/>

#### Else If

`elif` keyword should be placed at middle of if-statement (after `if`).

Also, you can use `elif` as many as you want.

Only the code block inside the first met condition will be executed. Then, jump to out of if-statement.

```Python
x = 5

if x > 10:
    print("x is greater than 10.")  # not met.
elif x > 5:
    print("x is greater than 5.")   # not met.
elif x == 5:
    print("x is 5.")                # run this.
elif x > 0:
    print("x is greater than 0.")   # ignored.
else:
    print("all conditions are not met.")    # ignored.
print("end of if-statement.")
```

output:

```
x is 5.
end of if-statement.
```

<br/>

#### Nested If-statement

`if` inside `if`, is called nested if-statement.

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

output:

```
x is greater than 0.
x is not greater than 10.
```

<br/>

#### Pass

if-statement cannot be empty, but you can put `pass` instead.

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

output:

```
end of if-statement.
```

<br/>

#### Conditional Expression

if-else statement can be written in one single line.

```Python
x = 5

print("x is 5.") if x == 5 else print("x is not 5")

# Same as
if x == 5:
    print("x is 5.")
else:
    print("x is not 5.")

# Also, another example.
a = 0
b = 10 if a == 0 else 20
print("b is " + str(b))        # 10
```

output:

```
x is 5.
x is 5.
b is 10
```

<br/>

## Loops
Python has two type of loops:
- `for` loops
- `while` loops

Flow chart:

```
                   ------------------------
                   |                      |
                   v      if True         |
Before ------> Conditions ------> Codes inside loop
                   |
                   |
                   |if False
                   -------------------> After
                   
```

<br/>

### For Loops

`for` loops can iterate all items in a sequence (iterable).

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
    print("finished!")      # after loop done.
```

output:

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

> built-in method `range(beg, end, step=1)` can create a number sequence.  
> `range(5)` -> `0 1 2 3 4`  
> `range(2, 5)` -> `2 3 4`  
> `range(0, 5, 2)` -> `0 2 4`  
> `range(5, 0, -1)` -> `5 4 3 2 1`

<br/>

### While Loops
`while` loops using condition to determine "keep looping" or "jump out".

formation of `while`:

```Python
while <condition>:
    <codes>
```

and

```Python
while <condition>:
    <codes, then go back to while>
else:
    <codes for condition is violated, then jump out>
```

Example:

```
# From 1 add to 100
count = 1
sum = 0

while count <= 100:
    sum += count
    count += 1

print("sum: " + str(sum))

print("---")

# With else
count = 1
sum = 0

while count <= 100:
    sum += count
    count += 1
else:
    print("while-loop is done and sum = " + str(sum))
```

output:

```
sum: 5050
---
while-loop is done and sum = 5050
```

<br/>

### Break
Using `break` can stop the loop and jump out immediately.

```Python
for i in range(10):
    print(i)
    
    if i == 3:
        break
```

output:

```
0
1
2
3
```

<br/>

### Continue
Using `continue` can skip the rest of codes and directly go to next iteration.

```Python
for i in range(10):
    if i % 2 == 1:
        continue
    
    print(i)
```

output:

```
0
2
4
6
8
```

<br/>

## One More Thing
Up to here, you can do lots of things with Python.

Do some practices to get it.



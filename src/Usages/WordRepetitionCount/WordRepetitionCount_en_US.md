# Word Repetition Count
[![Project link](../../../res/badges_project.svg)](https://github.com/FaDrYL/From0ToPython) 

[![Github link](../../../res/badges_github.svg)](https://github.com/FaDrYL)
[![Website link](../../../res/badges_website.svg)](https://www.fadryl.com/)

<br/>

To count word repetition in a text file.

[[Code Sample]](WordRepetitionCount.py)

<br/>

## Before Start
For each question, please think about it for yourself first.

<br/>

## Introduction
To do the counting, we need using something to store the words and their count.

> What data type do we need to achieve it?

<br/>

In this chapter, we will using "Dictionary" to store them with `(word: count)` format.

Because, every key is unique in dictionary which hasn't repetition.

Also, the value can be updated by the same key.

<br/>

## 💻 Time To Code
### Workflow
> What steps do we need to take to accomplish the goal?

1. Get the filename from input.
2. Read file and convert to dictionary.
3. To sort the dictionary and get the ranking.
4. Print the result out.

<br/>

### Get The File Name From Input
Using `input()` function with prompt to get the file name.

Also, using `strip()` function to avoid the leading and ending whitespace.

```Python
filename = input("Name of the text file to count? ").strip()
```

<br/>

### Read File And Convert To Dictionary
> How can we get words from a text file?

1. Open the file.
2. Get lines from file.
3. Get words from each line.
4. Remove all the punctuations from words.
5. Make the word to lower case to remove repetitions for word with different case.
6. Add/Update the word to/in dictionary.

```Python
# 1. Open the file. We just need to read it.
file = open(filename, "rt")

word_dict = dict()
# 2. Get lines from file.
for line in file:
    # 3. Get words from each line.
    for word in line.split():
        # 4. Remove all the punctuations from words.
        # we need to "import string"
        trans_table = word.maketrans("", "", string.punctuation)
        word = word.translate(trans_table)
        
        # 5. Make the word to lower case
        word = word.lower()
        
        # 6. Add/Update the word to/in dictionary.
        try:
            # try to update first
            word_dict[word] += 1
        except KeyError:
            # if not exist, add it to dict.
            word_dict[word] = 1
```

<br/>

### To Sort The Dictionary.
> How to sort the dictionary?

We can get a list of `(key: value)` pairs by `dict.items()` function.

Then, using `sorted()` function to sort the list. set the sorting key to the `value` in `(key: value)` pair which is index 1.

After that, we can get a sorted list of original dictionary in ascending order.

Also, We can use `reverse()` to make a ranking from the highest count to the lowest (descending).

```Python
sorted_word_list = sorted(word_dict.items(), key=lambda item: item[1])
sorted_word_list.reverse()
```

<br/>

### Print The Result Out
We can define the number of rankings that we need to print them out.

Also, Using `format()` function to format the string as a table.

```Python
# number of items to print
num_print = 10
# table format
str_format = "{0:^15} {1:<15} {2:<15}"

# print the header
print(str_format.format("Ranking", "Word", "Count"))

for i in range(num_print):
    # get the item in sorted list
    item = sorted_word_list[i]
    # print table formatted ranking, word, count
    print(str_format.format(i+1, item[0], item[1]))
```

## 🥂 Making Them Together
> How to make them together?

We just need to add some logic to make them together.

Putting them as functions is a good choice.

👉 [[Code Sample]](WordRepetitionCount.py) (do it before looking the sample)


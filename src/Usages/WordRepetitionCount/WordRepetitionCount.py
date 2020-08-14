"""
Author: FaDr_YL (_YL_)
"""


from typing import Dict, List
from string import punctuation


# type of filename is str; type of return value is dict.
def read_file_2_dict(filename: str) -> Dict:
    """Read words in the text file to dictionary.

    :param filename: Name of the text file.
    :return: Dictionary with (word: count).
    """
    print("Loading the file...")
    # read the text file
    file = open(filename, "rt")

    print("Counting...")
    word_dict = dict()
    for line in file:
        # read each line
        for word in line.split():
            # read words in this line
            # make a trans table to remove punctuations
            trans_table = word.maketrans("", "", punctuation)
            word = word.translate(trans_table)

            # make the word to lower case.
            word = word.lower()

            try:
                # try to + 1
                # raise error if the word is not found in word_dict.
                word_dict[word] += 1
            except KeyError:
                # add it to word_dict if has error.
                word_dict[word] = 1
    return word_dict


def sort_dict_desc(word_dict: Dict) -> List:
    """Sort the dictionary in descending order.

    :param word_dict: the dictionary of word.
    :return: sorted list of dictionary.
    """
    # sort by value
    # word_dict.items() to get a list of (key: value) pairs
    sorted_word_dict = sorted(word_dict.items(), key=lambda item: item[1])
    # descending order
    sorted_word_dict.reverse()
    return sorted_word_dict


def print_from_list(lst: List, num: int = 10, colored: bool = False) -> None:
    """Print results from the list.

    :param lst: list of results
    :param num: number of results to print
    :param colored: print the result with color, or not.
    """
    if num > len(lst):
        # if num is larger than length of lst.
        raise ValueError("\'num\' should smaller than or equal to length of \'lst\'")
    print()
    print("Top 10 words:")
    # string without color
    result_str = "{0:^15} {1:<15} {2:<15}"
    # color code
    style_1 = "\033[100m"
    style_reset = "\033[0m"
    # string with color
    result_str_colored = style_1 + "{0:^15}" + style_reset + " {1:<15}" + style_1 + " {2:<15}" + style_reset

    # determine which string.
    result_str = result_str_colored if colored else result_str
    # print table header
    print(result_str.format("Ranking", "Word", "Count"))
    for i in range(num):
        # only do 'num' times
        item = lst[i]
        # print table items
        print(result_str.format(i+1, item[0], item[1]))


def main():
    while True:
        # ask the filename from user.
        filename = input("Name of the text file to count\n"
                         "(or input 'q' or 'Q' to quit)\n"
                         "? ").strip()

        # if the input is 'q' or 'Q', stop the loop and quit.
        if filename.upper() == "Q":
            break

        try:
            # try to read the file from user's input.
            word_dict = read_file_2_dict(filename)
        except IOError:
            # if the file is not found.
            print("File is not found!")
            print("Please try again.")
            print()
            # ask the filename again
            continue
        else:
            # no error occur.
            print("Finished counting.")

        # sort the dict of results.
        sorted_word_list = sort_dict_desc(word_dict)
        # print the result out.
        print_from_list(sorted_word_list, colored=True)
        # no error and jump out.
        break
    # finish
    print("\n-----")
    print("Finished!")


if __name__ == "__main__":
    main()

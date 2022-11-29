"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    create name list in ans_list first and find anagrams
    """
    start = time.time()
    ####################
    name_list = read_dictionary(FILE)
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    input_name = input("Find anagrams for: ")
    while input_name != "-1":
        ans_list = find_anagrams(input_name, name_list)
        print(str(len(ans_list)) + " anagrams: " + str(ans_list))
        input_name = input("Find anagrams for: ")
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(file):
    name_list = []
    with open(file, "r") as f:
        for line in f:
            name_list.append(line[:-1])
    return name_list


def find_anagrams(s, name_list):
    """
    :param name_list: name list in the dictionary.txt
    :param s: input name
    :return: return the answer of the name list
    """
    ans_list = []
    print("Searching...")
    find_anagrams_helper(s, "", len(s), "", ans_list, name_list)
    return ans_list


def find_anagrams_helper(input_name, current_str, name_len, str_count, ans_list, name_list):
    if len(current_str) == name_len and current_str not in ans_list and current_str in name_list:
        ans_list.append(current_str)                    # if current_str in the ans_list and not be repeated before
        print("Found:", current_str)
        print("Searching...")
    else:
        for i in range(len(input_name)):
            if str(i) in str_count:
                pass
            elif current_str != "" and len(current_str) != 1 and not has_prefix(current_str, name_list):
                break                                   # if the beginning words are not in the name list
            else:
                # Choose
                current_str += input_name[i]
                str_count += str(i)
                # Explore
                find_anagrams_helper(input_name, current_str, name_len, str_count, ans_list, name_list)
                # Un-choose
                current_str = current_str[:-1]
                str_count = str_count[:-1]


def has_prefix(sub_s, name_list):
    """
    :param name_list: the name of the list
    :param sub_s: the name to be found if it has a word to start with
    :return: True/False
    """
    count = False                                           # to consider if it's the first character is checked
    for name in name_list:
        if name.startswith(sub_s[0]):
            count = True
            if name.startswith(sub_s):
                return True
        elif count:
            return False


if __name__ == '__main__':
    main()

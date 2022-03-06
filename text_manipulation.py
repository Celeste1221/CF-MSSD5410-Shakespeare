import fractions
import string
import re

# returns the txt file as a list of each line in the file, minus the first 3 lines
def process_file(fname, enc):
    # open file for reading 'r'
    with open(fname, 'r', encoding=enc) as file:
        lines = file.readlines()[3:] # read file in to a line by line list, discard the first 3 lines
    return lines


# roman_to_int code obtained from:
# https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php
# accessed on 3/5/22
# author: none given
def roman_to_int(s):  # TODO: this used to work and now it doesn't; KeyError: 'II'
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val


# takes in a list, returns a list of strings with each element being a roman numeral heading
def get_headings(lines):
    roman_num = []
    for i in range (len(lines)):
        # if the lines before and after are empty, add the line in the middle, which is the roman numeral heading
        if lines[i] == "\n" and lines[i+2] == "\n":
            # get rid of white space, convert elements to strings instead of lists
            roman_num.append(' '.join(lines[i+1].split()))
    return roman_num

# takes in a list of lists and returns one string of words with no white space or roman numerals
def get_list_of_words(lines):
    poems = ''.join(str(line) for line in lines)
    poems = re.sub(r'([IVXLC]+.)', '', poems)
    poems = poems.split()
    return poems

# this should return a list of sub-lists with each sub-list being one entire poem
def get_list_of_poems(lines):  # TODO
    poems = []
    poem = re.search('\n\n(.*?)\n\n', lines)
    poems.append(poem)
    return poems

def write_results(fname, data, enc):
    # open a file for writing 'w'
    with open(fname, 'w', encoding=enc) as file:
        file.write(data)

# stores the words and their counts in a dictionary
def words_to_dict(all_words, dictionary):
    for w in all_words:  # for each word
        w = clean_word(w)  # send word for cleaning (get rid of punctuation and make everything lowercase)
        if w in dictionary:  # if word was counted before
            dictionary[w] += 1  # increment count
        else:
            dictionary[w] = 1  # begin count for new word


# get rid of punctuation and make everything lowercase
def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")  # delete punctuation  TODO: this doesn't get rid of quotations i.e. "word or word"
    return word.lower()


# uses regular expressions to clean up chapter headings
def perform_re(text):
    text = re.sub(r'(CHAPTER) ([IVXLC]+.)', '\\1\\2', text)
    return text


# takes a file, returns a list of its words
def word_list(file):
    words = process_file(file, 'utf-8')
    return words


# takes a list, returns a dictionary with each unique word as the key and the count of that word as the value
def unique_words_dict(words):
    unique_words_counts = {}  # empty dictionary for unique words count
    words_to_dict(words, unique_words_counts)  # run through all words to get each word and count them
    return unique_words_counts


# takes a dictionary, returns a list of words that appear only once
def get_first_five(dictionary):
    # make a new list for the words that appear only one time in the text
    unique = []
    for key in dictionary.keys():
        if dictionary[key] == 1:
            unique.append(key)
    return unique[:5]


# return first five words in a list of words
def first_five(words):
    return words[:5]


# calculate the type to token ratio
def calc_TTR(unique_words, words):
    ttr = float(unique_words / words)
    return round(ttr, 3)


# find a word and its count in the text
def find_word(word, words):
    if word in words:
        count = words.count(word)
    else:
        count = 0
    return count


# calculate whether word count difference is less than 3000
def TTR_validity(difference):
    if difference <= 3000:
        return "These TTR values are between comparable texts."
    else:
        return "TTR is not a reliable comparison of lexical complexity for the chosen texts."


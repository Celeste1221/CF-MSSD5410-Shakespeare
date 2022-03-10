import fractions
import string
import re

# returns the txt file as a list of each line in the file, minus the first 3 lines
def process_file(fname, enc):
    # open file for reading 'r'
    with open(fname, 'r', encoding=enc) as file:
        lines = file.readlines()[3:]
    return lines

# LCS function obtained from:
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
# Accessed on: 2/22/22; 

# Dynamic Programming implementation of LCS problem

# takes 2 strings, returns a list of the length of the lowest common subsequence between the 2 strings
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# roman_to_int code obtained from:
# https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php
# accessed on 3/5/22
# author: none given
# takes a roman numeral string and converts it to an integer
def roman_to_int(s):  # TODO: this used to work and now it doesn't; KeyError: 'II'
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

# modified from above function - converts the list of chapter headings from roman numerals to ints and
# returns the list of ints
def romans_to_int(l):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ints = []
    for i in range(len(l)):
        int_val = 0
        for j in range (len(l[i])):
            if j > 0 and rom_val[l[i][j]] > rom_val[l[i][j - 1]]:
                int_val += rom_val[l[i][j]] - 2 * rom_val[l[i][j - 1]]
            else:
                int_val += rom_val[l[i][j]]
        ints.append(int_val)
    return ints

def clean_dict(dict):
    x = []
    for key in dict:
        l = dict[key].split()
        x.append(l)
    return x 
    
    
# takes in a list, returns a list of strings with each element being a roman numeral heading
def get_headings(lines):
    roman_num = []
    for i in range (len(lines)):
        # if the lines before and after are empty, add the line in the middle, which is the roman numeral heading
        if lines[i] == "\n" and lines[i+2] == "\n":
            # get rid of white space, convert elements to strings instead of lists
            roman_num.append(' '.join(lines[i+1].split()))
    return roman_num

# takes in an array of of arrays of strings and returns a dictionary with roman numerals: poems
def get_poems(lines):
    poems = ''.join(str(line) for line in lines)
    poems = poems.split('\n\n')
    # convert list of roman numerals and poems into dict with roman numerals as keys and poems as values
    poems = {poems[i].strip(): poems[i + 1].strip() for i in range(0, len(poems), 2)}
    return poems

# takes a list, returns a dictionary with each unique word as the key and the count of that word as the value
def unique_words_dict(words):
    unique_words_counts = {}  # empty dictionary for unique words count
    words_to_dict(words, unique_words_counts)  # run through all words to get each word and count them
    return unique_words_counts

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

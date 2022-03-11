import fractions
import string
import re

# returns the txt file as a list of each line in the file, minus the first 3 lines
def process_file(fname, enc):
    # open file for reading 'r'
    with open(fname, 'r', encoding=enc) as file:
        lines = file.readlines()[3:]
    return lines

# roman_to_int code obtained from:
# https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php
# accessed on 3/5/22
# author: none given
# takes a roman numeral string and converts it to an integer
def roman_to_int(s):
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

# gets rid of caps, punctuation, and white space in a string
def clean_str(a_str):
    for p in string.punctuation:
        a_str   = a_str.replace(p, "")
    return a_str.lower().split()

# gets rid of caps, punctuation, and white space in the values of a dictionary
def clean_dict(dictionary):
    for key in dictionary:
        dictionary[key] = dictionary[key].lower().split()
        for word in dictionary[key]:
            for p in string.punctuation:
                word = word.replace(p, "")
    return  dictionary
    
# takes in a list, returns a list of strings with each element being a roman numeral heading
def get_headings(lines):
    roman_num = []
    for i in range (len(lines)):
        # if the lines before and after are empty, add the line in the middle, which is the roman numeral heading
        if lines[i] == "\n" and lines[i+2] == "\n":
            # get rid of white space, convert elements to strings instead of lists
            roman_num.append(' '.join(lines[i+1].split()))
    return roman_num

# takes in an list of of lists of strings and returns a dictionary with roman numerals: poems
def get_poems(lines):
    poems = ''.join(str(line) for line in lines)
    poems = poems.split('\n\n')
    # convert list of roman numerals and poems into dict with roman numerals as keys and poems as values
    poems = {poems[i].strip(): poems[i + 1].strip() for i in range(0, len(poems), 2)}
    return poems


# LCSubStr() (iterative implementation) obtained from:
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
# accessed on 3/10/22
# author: This code is contributed by Soumen Ghosh
# CHANGELOG:
# - removed redundant parentheses and driver code
# Python3 implementation of Finding
# Length of Longest Common Substring
# Returns length of longest common
# substring of X[0..m-1] and Y[0..n-1]
def LCSubStr(X, Y, m, n):

    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result

# This code is contributed by Soumen Ghosh


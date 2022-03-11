# text is "Shakespeare's Sonnets by William Shakespear"
# from: https://www.gutenberg.org/ebooks/1041

import string
from text_manipulation import *


# ask user to choose to input some text from a sonnet or the sonnet number
def get_user_input():
    choice = input("\nWelcome to the Shakespeare sonnet search. To find a sonnet, you can enter\n"
                   "the number of the sonnet, or you can enter a few words of the sonnet."
                   "\n(press q to quit)\n").lower()
    if choice is not int:
        return choice
    else:
        return int(choice)


# returns the index of the largest number in a list of integers
def largest_number(arr):
    largest = arr[0] # the value at the first index in the array
    for i in range(len(arr)):
        if largest < arr[i]:
            largest = arr[i]
    # for testing:
    # print("longest common substring is: " + str(largest))
    index = arr.index(largest)
    return index


def main():
    
    while True:
        # read in the file as an array where each element is one line of the poem (discard the first 3 lines)
        list_of_lines = process_file('shakespeare_sonnets.txt', 'utf-8')

        # pull just the roman numerals from the text and put them into a list
        roman_num = get_headings(list_of_lines)

        # convert the list of roman numerals to a list of integers
        numbers = romans_to_int(roman_num)

        # returns a dict with the text's roman numerals as keys and the sonnets as values
        poems = get_poems(list_of_lines)

        # change dictionary keys from roman numerals to ints to match user input options
        poems = dict(zip(numbers, list(poems.values())))
        # make a second dictionary to keep original formatting for final output
        poems1 = dict(zip(numbers, list(poems.values())))


        # user can input either a few words a sonnet or the number of the sonnet
        # to see the sonnet, or press q to quit
        choice = get_user_input()
        if choice == 'q':
            print("Goodbye.")
            break
        elif choice.strip().isdigit():
            choice = int(choice)
            if choice in poems.keys():
                print("Here is sonnet " + str(choice) + ":")
                print(poems[choice])
            else:
                print("Invalid input")
        elif choice is not int and choice != "": # choice is a string, so find lowest common substring
            # make list for the lengths of the longest common substrings for user input and each poem
            common = [] 
            # get rid of white space, caps, punctuation in user input
            choice = clean_str(choice)
            # get rid of white space, caps, punctuation in each poem
            cleaned_poems = clean_dict(poems)
            
            for poem in cleaned_poems:
                # returns the length of the longest common substring between choice and each poem
                longest = LCSubStr(choice, cleaned_poems[poem], len(choice), len(cleaned_poems[poem]))
                common.append(longest)

            # for testing:
            # print(common)

            # get the index of the largest element in common[], add 1 to get the dictionary key of the poem to return
            index = largest_number(common)
            if common[index] > 0:
                print("Here is sonnet " + str(index + 1) + ":")
                print(poems1[index + 1])
            else:
                print("Could not find your sonnet.")

if __name__ == "__main__":
    main()
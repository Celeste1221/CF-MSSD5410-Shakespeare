# text is from: https://www.gutenberg.org/ebooks/1041

from text_manipulation import *

# ask user to choose to input some text from a sonnet or the sonnet number
def get_user_input():
    choice = input("\nWelcome to the Shakespeare sonnet search. You can either enter\n"
                    "the number of the sonnet you would like to read, or if you don't know it\n"
                    "you can enter a few words of the poem. \nWhich sonnet would you like to see? "
                   "(press q to quit)\n").lower()
    if choice is not int:
        return choice
    else:
        return int(choice)


def main():
    
    while True:
        # read in the file as a list of sublists where each sublist is one line
        list_of_lines = process_file('shakespeare_sonnets.txt', 'utf-8')

        # gets a list of just the roman numerals in the text
        roman_num = get_headings(list_of_lines)

        # should convert the list of roman numerals into integers
        numbers = roman_to_int(roman_num)  ### TODO: this used to work and now it doesn't

        # should break down the list of poem lines to separate a chunk of lines wherever there is "\n\n",
        # then put them into a new list of poems
        poems = get_list_of_poems(list_of_lines)  ### TODO: doesn't work, I think regex I tried is bad

        # should combine the numbers list as keys and the poems list as values in a dictionary
        dictionary = {numbers[i]: poems[i] for i in range(0, len(poems))}
        
        # user can input either a few words or lines of a sonnet or the number of the sonnet
        # and then search the text for the poem or press q to quit
        choice = get_user_input()

        if choice == 'q':
            print("Goodbye.")
            break
        if choice is int:
            # iterate through keys to match the number
            if choice in dictionary.keys():
                print(dictionary[choice][value])
            else:
                print("Invalid input")   
        else:
            # iterate through dictionary values to find the element with the longest common subsequence
            # lcs = get_lcs(choice, dictionary[i][element]) for i in range (len(dictionary))
            if lcs > 0.5:
                pass # print that element
            else:
                # it's not close enough to be valid
                print("Shakespeare didn't write that.")

    
if __name__ == "__main__":
    main()
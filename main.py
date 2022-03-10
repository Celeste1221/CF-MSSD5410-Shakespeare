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
        # read in the file as an array where each element is one line of the poem (discards the first 3 lines)
        list_of_lines = process_file('shakespeare_sonnets.txt', 'utf-8')

        # pulls just the roman numerals from the text and puts them into a list
        roman_num = get_headings(list_of_lines)

        # converts the list of roman numerals to a list of integers
        numbers = romans_to_int(roman_num)

        # returns a dict with the text's roman numerals as keys and poems as values
        poems = get_poems(list_of_lines)

        # change dictionary keys from roman numerals to ints to match user input options
        poems = dict(zip(numbers, list(poems.values())))

        # user can input either a few words or lines of a sonnet or the number of the sonnet
        # to get back the sonnet or press q to quit
        choice = get_user_input()

        if choice == 'q':
            print("Goodbye.")
            break
        if choice.strip().isdigit():
            choice = int(choice)
            if choice in poems.keys():
                print(poems[choice])
            else:
                print("Invalid input")
        else:
            choice = choice.split()
            print(choice)
            common = []
            for poem in poems:
                longest = lcs(choice, poems[poem].split())
                common.append(longest)
                print(poems[poem].split())
            print(choice)
            print(common)
            # common should be a list of the lcs for each poem. Then we could find the highest lcs
            # in the list and get the poem at that index to print for the user

if __name__ == "__main__":
    main()
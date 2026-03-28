# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    # Add your code here #
    ######################
    total = 0
    names_file = open('names.txt', 'r')
    name = names_file.readline()
    while name != '':
        total += 1
        name = names_file.readline()

    print('There are ' + str(total) + ' names in the file.')

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
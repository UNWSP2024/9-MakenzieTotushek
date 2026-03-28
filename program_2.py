# Author: Makenzie Totushek
# Date: 3/27/2026
# Name: Random Number File

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
def random_number_file():
    number = random.randint(1, 500)
    random_number = open ('random_numbers.txt', 'w')
    amount = input('How many random numbers would you like added to the file (up to 1000)? ')
    for i in range(int(amount)):
        random_number.write(str(number) + '\n')
        number = random.randint(1, 500)
    print('The numbers were added to the file!')
if __name__ == '__main__':
    random_number_file()

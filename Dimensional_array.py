# Created by: Tochukwu Iroakazi
# Created on: Nov-2017
# Created for: ICS3U
# This program displays the average of a 2D array with random numbers

from numpy import random

def loop_average(array):
    # finds average in passed 2D array
    total = 0
    
    for row in array:
      for column in row:
          total = total + column
    average = total / (len(array[0]) * len(array))
    
    return average

# input
rows_number = int(raw_input('Enter the number of rows you want: '))
while rows_number < 0:
    print ('Please type in a valid number')
    rows_number = int(raw_input('Enter the number of rows you want: '))


columns_number = int(raw_input('Enter the number of columns you want: '))
while columns_number < 0:
    print('Please type in a valid number')
    columns_number = int(raw_input('Enter the number of columns you want: '))
    
# process
table = []

for rows in range(0, rows_number):
    table.append([])
    for columns in range(0, columns_number):
        table[rows].append(random.randint(0, 51))
        
average_of_elements_table = loop_average(table)

# output
print(table)
print('The average of the numbers in the table is ' + str(average_of_elements_table) + '.\n')

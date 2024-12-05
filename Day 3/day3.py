import re

# Part 1
def read_file(filename):
    infile = open(filename, 'r')
    line = infile.readline()
    mul_list = []
    
    while line != '':

        # RegEx to match function correctly - \d checks if it is a digit and {1,3} makes sure it is 1 - 3 digits long
        # https://www.w3schools.com/python/python_regex.asp
        x = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
        mul_list.append(x)
        line = infile.readline()

    return mul_list

def mul(num1, num2):
    return num1 * num2


mul_list = read_file('input.txt')

total = 0

for line in mul_list:
    for func in line:
        
        # Get function arguments by spliting at ( to get arguments in 1 index
        # Removing the ) by splicing using :-1
        # Then spliting that at , to get arguments in 0 and 1 index
        args = func.split('(')[1][:-1].split(',')
        
        if args[0].isnumeric() and args[1].isnumeric():
            num1 = int(args[0])
            num2 = int(args[1])
            total += mul(num1, num2)

print("Part 1:", total)

# ------------------- Part 2 -------------------
def read_file_conditional(filename):
    infile = open(filename, 'r')
    line = infile.readline()
    mul_list = []
    do_list = []
    new_string = ""

    # Combine string from file without line breaks
    while line != '':
        combine = line.strip('\n')
        new_string += combine
        line = infile.readline()


    # Start 'do()' search for mul from 0, ending at first occurence of 'don't()'
    start_index = 0
    end_index = new_string.find('don\'t()')
    substring = new_string[start_index:end_index + 7]

    # If there is a 'do()' and a 'don't()' still present
    while start_index != -1 and end_index != -1:

        # Append the substring between the 'do()' and 'don't()' to the list
        do_list.append(substring)

        # Set the next substring start index to the first occurence of 'do()' after the previous 'don't()'
        start_index = new_string.find('do()', end_index)
        end_index = new_string.find('don\'t()', start_index)
        substring = new_string[start_index:end_index + 7]

    # Loop through list of substrings added to the list, and run RegEx checks as done in Part 1
    for sub in do_list:
       x = re.findall("mul\(\d{1,3},\d{1,3}\)", sub)
       for func in x:
           mul_list.append(func)  

    return mul_list

mul_list_conditional = read_file_conditional('input.txt')

conditional_total = 0

for func in mul_list_conditional:

    # Get function arguments by spliting at ( to get arguments in 1 index
    # Removing the ) by splicing using :-1
    # Then spliting that at , to get arguments in 0 and 1 index
    args = func.split('(')[1][:-1].split(',')

    if args[0].isnumeric() and args[1].isnumeric():
        num1 = int(args[0])
        num2 = int(args[1])
        conditional_total += mul(num1, num2)

print("Part 2:", conditional_total)
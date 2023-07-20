with open('password.txt', 'r') as input_file:
    # read all the numbers as a single string
    num_string = input_file.read()

# split the numbers by space into a list
num_list = num_string.split()

# open output file for writing
with open('password_new.txt', 'w') as output_file:
    # iterate over the numbers in the list and write each one on a new line
    for num in num_list:
        output_file.write(num + '\n')
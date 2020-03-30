file_text = open('data.dat') # open file
file_text = file_text.read() # read it's content
file_text = file_text[:-1] # Delete the last line which is empty

file_text = file_text.split('\n') # split it when it changes line


counter = 0

for current_line in file_text:

    zeros_number = current_line.count('0') # Current line's 0s
    ones_number = current_line.count('1') # Current line's 1s
    
    
    if (zeros_number % 3 == 0) or (ones_number % 2 == 0):
        counter += 1 # counter = counter + 1


print(counter)
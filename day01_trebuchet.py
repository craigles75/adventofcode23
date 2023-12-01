
import re
input_file = open("day01_input.txt", 'r');

total_number = 0

for input_line in input_file:
    print(input_line)
    #replace words with numbers
    input_line = re.sub(r"one", "o1e", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"two", "t2o", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"three", "t3e", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"four", "f4r", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"five", "f5e", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"six", "s6x", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"seven", "s7n", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"eight", "e8t", input_line, flags=re.IGNORECASE)
    input_line = re.sub(r"nine", "n9e", input_line, flags=re.IGNORECASE)

    numbers = re.findall(r'\d', input_line)
    added_numbers = numbers[0] + numbers[-1]
    total_number += int(added_numbers)

print (total_number)


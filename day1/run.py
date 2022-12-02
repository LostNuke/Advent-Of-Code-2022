input_file = open('input.txt')
input_lines = input_file.readlines()

first_biggest_number = 0
second_biggest_number = 0
third_biggest_number = 0

current_counter = 0

elf_counter = 0

for line in input_lines:
    if line.strip() == "":
        elf_counter += 1
        print("First: {} - second: {} - third: {} - current: {}".format(first_biggest_number, second_biggest_number, third_biggest_number, current_counter))
        if first_biggest_number <= current_counter:
            third_biggest_number = second_biggest_number
            second_biggest_number = first_biggest_number
            first_biggest_number = current_counter
        elif second_biggest_number <= current_counter:
            third_biggest_number = second_biggest_number
            second_biggest_number = current_counter
        elif third_biggest_number <= current_counter:
            third_biggest_number = current_counter
        current_counter = 0
    else:
        # print("number: {} - raw: {}".format(int(line.strip()), line.strip()))
        current_counter += int(line.strip())

print(first_biggest_number+second_biggest_number+third_biggest_number)
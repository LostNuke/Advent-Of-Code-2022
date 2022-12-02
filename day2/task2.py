input_file = open('input.txt')
input_lines = input_file.readlines()

points = 0

for line in input_lines:
    line = line.strip()
    if 'Y' in line:
        points += 3
        if 'A' in line:
            points += 1
        elif 'B' in line:
            points += 2
        elif 'C' in line:
            points += 3
    elif 'X' in line:
        points += 0
        if 'A' in line:
            points += 3
        elif 'B' in line:
            points += 1
        elif 'C' in line:
            points += 2
    elif 'Z' in line:
        points += 6
        if 'A' in line:
            points += 2
        elif 'B' in line:
            points += 3
        elif 'C' in line:
            points += 1
print(points)
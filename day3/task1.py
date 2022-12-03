import os, os.path, shutil
input_file = open('input.txt')
input_lines = input_file.readlines()

point = 0

for line in input_lines:
    shutil.rmtree('./backpack/')
    os.mkdir('./backpack/')
    compartment_one = line[0:int(len(line)/2)]
    compartment_one = set(list(compartment_one))

    compartment_two = line[int(len(line)/2):len(line)-1]
    compartment_two = set(list(compartment_two))

    for item_in_one in compartment_one:
        try:
            open('./backpack/{}'.format(ord(item_in_one)), 'x')
        except:
            continue
    
    for item_in_two in compartment_two:
        try:
            open('./backpack/{}'.format(ord(item_in_two)), 'x')
        except:
            if ord(item_in_two) < 97:
                print('Raw Ascii: {} - Letter: {} - After: {}'.format(ord(item_in_two), item_in_two, ord(item_in_two)-38))
                point += ord(item_in_two)-38
            else:
                print('Raw Ascii: {} - Letter: {} - After: {}'.format(ord(item_in_two), item_in_two, ord(item_in_two)-96))
                point += ord(item_in_two)-96
print(point)
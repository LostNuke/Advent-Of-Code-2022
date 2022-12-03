import os, os.path, shutil, re
input_file = open('input.txt')
input = input_file.read()

point = 0

ungrouped_array = re.findall('((?:[^\n]+\n?){1,3})', input)
for ungrouped_backpack in ungrouped_array:

    backpack = ungrouped_backpack.split('\n')
    shutil.rmtree('./backpack/')
    os.mkdir('./backpack/')

    collision_one = ''


    # Get all Colliding Items between backpack 1 and 2
    for item in set(backpack[0]):
        try:
            open('./backpack/{}'.format(ord(item)), 'x')
        except:
            continue
    for item in set(backpack[1]):
        try:
            open('./backpack/{}'.format(ord(item)), 'x')
        except Exception as e:
            collision_one += item

    shutil.rmtree('./backpack/')
    os.mkdir('./backpack/')

    collision_two = ''

    for item in set(backpack[1]):
        try:
            open('./backpack/{}'.format(ord(item)), 'x')
        except:
            continue
    for item in set(backpack[2]):
        try:
            open('./backpack/{}'.format(ord(item)), 'x')
        except:
            collision_two += item

    shutil.rmtree('./backpack/')
    os.mkdir('./backpack/')

    for item in collision_one:
        try:
            open('./backpack/{}'.format(ord(item)), 'x')
        except:
            continue
    for item in collision_two:
        try:
            open('./backpack/{}'.format(ord(item)), 'x')
        except:
            if ord(item) < 97:
                point += ord(item)-38
            else:
                point += ord(item)-96
    
print(point)
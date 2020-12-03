def main():

    mountain = []
    mountain_long = []

    # Populate the initial mountain from our input file
    with open('input.txt') as file:
        for line in file:
            mountain.append(line.rstrip('\n'))
    
    # The initial input was just a short version of the mountain
    # To have enough distance to make it to the bottom, we need to expand it lengthwise
    for item in mountain:
        item = item*100
        mountain_long.append(item)
    
    # A version of the mountain with every other item skipped (to be able go down by 2)
    mountain_long_skipped = mountain_long[::2]

    r1d1_pos = 0
    r1d1_tree_count = 0

    r3d1_pos = 0
    r3d1_tree_count = 0

    r5d1_pos = 0
    r5d1_tree_count = 0

    r7d1_pos = 0
    r7d1_tree_count = 0

    r1d2_pos = 0
    r1d2_tree_count = 0

    # Iterate through the layers of the mountain, sliding 3 positions right each time
    # By iterating through the items in the list we also slide one layer down each time
    # If there is a tree '#' at that location, add it to the tree count
    # RIGHT 1, DOWN 1
    for item in mountain_long:
        if item[r1d1_pos] == '#':
            r1d1_tree_count += 1
        r1d1_pos += 1

    # RIGHT 3, DOWN 1
    for item in mountain_long:
        if item[r3d1_pos] == '#':
            r3d1_tree_count += 1
        r3d1_pos += 3

    # RIGHT 5, DOWN 1
    for item in mountain_long:
        if item[r5d1_pos] == '#':
            r5d1_tree_count += 1
        r5d1_pos += 5

    # RIGHT 7, DOWN 1
    for item in mountain_long:
        if item[r7d1_pos] == '#':
            r7d1_tree_count += 1
        r7d1_pos += 7

    # RIGHT 1, DOWN 2
    # Uses mountain_long_skipped, defined in line 18 above
    for item in mountain_long_skipped:
        if item[r1d2_pos] == '#':
            r1d2_tree_count += 1
        r1d2_pos += 1

    print('Right 1, down 1 tree count: ' + str(r1d1_tree_count))
    print('Right 3, down 1 tree count: ' + str(r3d1_tree_count))
    print('Right 5, down 1 tree count: ' + str(r5d1_tree_count))
    print('Right 7, down 1 tree count: ' + str(r7d1_tree_count))
    print('Right 1, down 2 tree count: ' + str(r1d2_tree_count))
    print('Multiplied together, these values yield: ' + str(r1d1_tree_count * r3d1_tree_count * r5d1_tree_count * r7d1_tree_count * r1d2_tree_count))

main()
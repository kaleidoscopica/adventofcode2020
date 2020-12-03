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
        item = item*40
        mountain_long.append(item)

    right_pos = 0
    tree_count = 0

    # Iterate through the layers of the mountain, sliding 3 positions right each time
    # By iterating through the items in the list we also slide one layer down each time
    # If there is a tree '#' at that location, add it to the tree count
    for item in mountain_long:
        if item[right_pos] == '#':
            tree_count += 1
        right_pos += 3

    print(tree_count)

main()
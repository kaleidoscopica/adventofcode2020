import re

def main():

    luggage_rules = []

    with open('input.txt') as file:
        for line in file:
            luggage_rules.append(line.rstrip('\n'))

    bags = []
    bags_len_before = 0
    bags_len_after = 0

    for item in luggage_rules:
        if 'shiny gold' in item:
            if 'shiny gold bags contain' not in item:
                type_of_bag = item.split(' bags')[0]
                bags.append(type_of_bag)

    bags_len_before = len(bags)
    while bags_len_before != bags_len_after:
        bags_len_before = len(bags)
        for item in luggage_rules:
            for bag in bags:
                if bag in item:
                    if bag + ' bags contain' not in item:
                        type_of_bag = item.split(' bags')[0]
                        if type_of_bag not in bags:
                            bags.append(type_of_bag)
        bags_len_after = len(bags)

    bag_count = len(bags)
    print(bag_count)

main()
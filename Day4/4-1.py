def main():

    passports = []
    valid_passport_count = 0

    # Populate the initial passport list from our input file
    with open('input.txt') as file:
        passports = file.read()
    
    passports = passports.split("\n\n") #creates a separate item in the list 
    passports = [item.replace('\n', ' ') for item in passports] #merges single newlines together
    passports = [item.split(' ') for item in passports] #splits each item separated by a space

    # Now each 'person' has a nested list of their passport values
    # example:
    # ['eyr:2029', 'iyr:2013', 'hcl:#ceb3a1', 'byr:1939', 'ecl:blu', 'hgt:163cm', 'pid:660456119']

    # Now iterate through the nested lists in passports, creating a dictionary for each,
    # then checking that all necessary keys exist in each dictionary
    for line in passports:
        passport_dict = dict(item.split(':') for item in line)
        # if all the keys (except cid) are in a passport, count it as valid
        if 'byr' in passport_dict:
            if 'iyr' in passport_dict:
                if 'eyr' in passport_dict:
                    if 'hgt' in passport_dict:
                        if 'hcl' in passport_dict:
                            if 'ecl' in passport_dict:
                                if 'pid' in passport_dict:
                                    valid_passport_count += 1

    print(valid_passport_count)

main()
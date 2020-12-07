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

        is_birthyear_valid = False
        is_issueyear_valid = False
        is_expiryyear_valid = False
        is_height_valid = False
        is_haircolor_valid = False
        is_eyecolor_valid = False
        is_passportid_valid = False

        if 'byr' in passport_dict and len(passport_dict['byr']) == 4 and int(passport_dict['byr']) >= 1920 and int(passport_dict['byr']) <= 2002:
            is_birthyear_valid = True

        if 'iyr' in passport_dict and len(passport_dict['iyr']) == 4 and int(passport_dict['iyr']) >= 2010 and int(passport_dict['iyr']) <= 2020:
            is_issueyear_valid = True

        if 'eyr' in passport_dict and len(passport_dict['eyr']) == 4 and int(passport_dict['eyr']) >= 2020 and int(passport_dict['eyr']) <= 2030:
            is_expiryyear_valid = True

        if 'hgt' in passport_dict:
            is_height_valid = True
            if passport_dict['hgt'][-2:] == 'cm':
                if int(passport_dict['hgt'][:-2]) < 150 or int(passport_dict['hgt'][:-2]) > 193:
                    is_height_valid = False
            elif passport_dict['hgt'][-2:] == 'in':
                if int(passport_dict['hgt'][:-2]) < 59 or int(passport_dict['hgt'][:-2]) > 76:
                    is_height_valid = False
            else:
                is_height_valid = False

        if 'hcl' in passport_dict and passport_dict['hcl'][0] == '#' and len(passport_dict['hcl']) == 7:
            is_haircolor_valid = True
            for char in passport_dict['hcl'][1:]:
                if char != 'a' and char != 'b' and char != 'c' and char != 'd' and char != 'e' and char != 'f' \
                    and char != '0' and char != '1' and char != '2' and char != '3' and char != '4' and char != '5' \
                    and char != '6' and char != '7' and char != '8' and char != '9':
                    is_haircolor_valid = False

        if 'ecl' in passport_dict and (passport_dict['ecl'] == 'amb' or passport_dict['ecl'] == 'blu' \
            or passport_dict['ecl'] == 'brn' or passport_dict['ecl'] == 'gry' or passport_dict['ecl'] == 'grn' \
            or passport_dict['ecl'] == 'hzl' or passport_dict['ecl'] == 'oth'):
            is_eyecolor_valid = True

        if 'pid' in passport_dict and len(passport_dict['pid']) == 9:
            is_passportid_valid = True

        if is_birthyear_valid == True and is_issueyear_valid == True and is_expiryyear_valid == True and is_height_valid == True \
            and is_haircolor_valid == True and is_eyecolor_valid == True and is_passportid_valid == True:
            valid_passport_count += 1

    print(valid_passport_count)

main()
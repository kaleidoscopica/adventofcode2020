def main():

    passwords = []

    # 'with open as file' will take care of closing the file afterward,
    # so there's no need to close it manually
    with open('input.txt') as file:
        for line in file:
            passwords.append(line.rstrip('\n'))

    password_check = []
    for item in passwords:
        item = item.replace(':', '')
        password_check.append(item.split(' '))

    valid_passwords_count = 0

    for item in password_check:
        interval = []
        interval.extend(item[0].split('-'))
        first_char = int(interval[0])
        second_char = int(interval[1])
        password_policy = item[1]
        password = item[2]
        count = 0

        if password[first_char-1] == password_policy:
            count += 1
        if password[second_char-1] == password_policy:
            count += 1
        
        if count == 1:
            valid_passwords_count += 1

    print(valid_passwords_count)

main()
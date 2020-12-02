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
        int_start = int(interval[0])
        int_end = int(interval[1])
        password_policy = item[1]
        password = item[2]
        count = 0

        for char in password:
            if char == password_policy:
                count += 1
        
        if count >= int_start and count <= int_end:
            valid_passwords_count += 1

    print(valid_passwords_count)

main()
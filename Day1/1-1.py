def main():

    file = open('input.txt', 'r')
    file_to_list = file.readlines()

    for line in file_to_list:
        num1 = int(line)
        
        for line2 in file_to_list:
            sum = 0
            num2 = int(line2)
            sum = num1 + num2

            if sum == 2020:
                print(sum)
                multiplied_total = num1 * num2
                print(multiplied_total)

    file.close()

main()
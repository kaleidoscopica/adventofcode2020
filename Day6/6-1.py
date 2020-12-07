def main():

    customs_questions = []
    count = 0

    with open('input.txt') as file:
        customs_questions = file.read()

    customs_questions = customs_questions.split("\n\n") #creates a separate item in the list 
    customs_questions = [item.replace('\n', '') for item in customs_questions] #merges single newlines together

    for item in customs_questions:
        tmp_list = []
        for char in item:
            if char not in tmp_list:
                tmp_list.append(char)
        count += len(tmp_list)

    print(count)

main()
def main():

    customs_questions = []
    count = 0

    with open('input.txt') as file:
        customs_questions = file.read()

    customs_questions = customs_questions.split("\n\n") #creates a separate list within the list for each group
    customs_questions = [item.split('\n') for item in customs_questions] #splits each item separated by a newline

    # Iterate through each group
    for lst in customs_questions:
        list_length = len(lst) #get the group length (number of people who answered)
        joined_items = ''.join(lst) #then join the questionnaire answers together

        # Using dict.get() to get a count of each element in a string
        # If the previously occurring character is new, it assigns 0 as initial and appends 1 to it, 
        # else it appends 1 to the previously held value of that element in the 'result' dictionary
        result = {}
        for keys in joined_items: 
            result[keys] = result.get(keys, 0) + 1
            # If a letter's count (result[keys]) equals the number of people in that group, increase the count
            if result[keys] == list_length:
                count += 1

    print(count)

main()
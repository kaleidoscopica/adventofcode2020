def main():

    boarding_passes = []
    seat_ids = []
    highest_seat_id = 0
    my_seat = 0

    with open('input.txt') as file:
        for line in file:
            boarding_passes.append(line.rstrip('\n'))
    
    for item in boarding_passes:
        seat_row = parse_row(item)
        seat_column = parse_column(item)
        seat_id = seat_row * 8 + seat_column
        seat_ids.append(seat_id)

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    
    seat_ids = sorted(seat_ids)
    my_seat = find_missing(seat_ids)

    print(my_seat)

def parse_row(input):
    row_counter = 0

    if input[0] == 'B':
        row_counter += 64
    if input[1] == 'B':
        row_counter += 32
    if input[2] == 'B':
        row_counter += 16
    if input[3] == 'B':
        row_counter += 8
    if input[4] == 'B':
        row_counter += 4
    if input[5] == 'B':
        row_counter += 2
    if input[6] == 'B':
        row_counter += 1
    
    return row_counter

def parse_column(input):
    column_counter = 0

    if input[7] == 'R':
        column_counter += 4
    if input[8] == 'R':
        column_counter += 2
    if input[9] == 'R':
        column_counter += 1
    
    return column_counter

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst] 

main()
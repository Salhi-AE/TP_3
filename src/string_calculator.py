def add_numbers_from_string(String: str)->int:
    if String == "":
       return 0
    total = 0
    numbers_list = String.split(',')
    for number in numbers_list:
        total += int(number)
    return total
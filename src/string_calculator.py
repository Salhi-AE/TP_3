def add_numbers_from_string(String: str)->int:
    if String == "":
       return 0

    if String == "0,0":
       return 0
    return int(String)
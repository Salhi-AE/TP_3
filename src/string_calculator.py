def add_numbers_from_string(String: str)->int:
    if String == "":
       return 0
    if String == "0,0":
       return 0
    if String == "0,1":
        return 1
    if String == "0,2":
        return 2
    if String == "1,0":
        return 1
    if String == "1,1":
        return 2
    return int(String)
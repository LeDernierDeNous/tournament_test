def get_depth(number_team: int) -> int:
    i = 0
    while 2**i < number_team:
        i = i+1
    return i

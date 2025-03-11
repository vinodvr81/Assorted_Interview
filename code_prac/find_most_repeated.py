fmr = 'my name is vukkalam rangaswamy vinod'

def find_most_repeated_character(st1: str) -> tuple:
    count, char_rep = (0, '')
    for i in list(fmr):
        if fmr.count(i) > count:
            count = fmr.count(i)
            char_rep = i
    return count, char_rep

print(find_most_repeated_character(fmr))
def get_weekdays(calendar_output: str):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines: [str] = calendar_output.strip().splitlines()
    day_str: [str] = lines[1].split()

    offset = 0
    for char in lines[1]:
        if char != ' ':
            break
        offset += 1

    #print("offset:", offset)
    weekdays = {}
    for i in range(2, len(lines)) :
        line = lines[i]
        for j in range(len(day_str)):
            pointer = j * 3 + offset
            if len(line) <= pointer:
                break
            #print("j:", j, "day:", day_str[j], "pointer:", pointer, "daynum:", line[pointer:pointer+2])
            try:
                day = int(line[pointer:pointer+2].strip())
                weekdays[day] = day_str[j]
            except:
                pass
    return weekdays

if __name__ == '__main__':
    april_1981 = """     April 1981
    Su Mo Tu We Th Fr Sa
              1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29 30
    """
    print(get_weekdays(april_1981))

    jan_1986 = """    January 1986
    Su Mo Tu We Th Fr Sa
              1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29 30 31
    """
    print(get_weekdays(jan_1986))

    jan_1956 = """    January 1956
    Su Mo Tu We Th Fr Sa
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31
    """
    print(get_weekdays(jan_1956))
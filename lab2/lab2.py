def char_frequency(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] = dict[n] + 1
        else:
            dict[n] = 1
    return dict

str = input("Please enter the string:")
print(char_frequency(str))

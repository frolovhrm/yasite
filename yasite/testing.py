def to_camel_case(text):
    if text.find('-'):
        test_split = text.split('-')
    else:
        test_split = text.split('_')
    print(test_split)
    i = len(test_split)
    print(i)
    new_text = ''
    if i > 1:
        n = 2
        while n <= i:
            word = test_split[n - 1]
            word = word.title()
            test_split[n - 1] = word
            n += 1
        new_text = ''.join(test_split)

    return new_text


# print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))

numerals = [
    {'letter': 'M', 'value': 1000},
    {'letter': 'D', 'value': 500},
    {'letter': 'C', 'value': 100},
    {'letter': 'L', 'value': 50},
    {'letter': 'X', 'value': 10},
    {'letter': 'V', 'value': 5},
    {'letter': 'I', 'value': 1},
    ]

def arabic_to_roman(number):
    remainder = number
    result = ''
    for numeral_index in range(len(numerals)):
        numeral = numerals[numeral_index]
        next_numeral = numerals[numeral_index + 1] if numeral_index + 1 < len(numerals) else None

        factor = int(remainder / numeral['value'])
        remainder -= factor * numeral['value']

        if next_numeral:
            numeral_difference = numeral['value'] - next_numeral['value']
            if (remainder - numeral_difference >= 0) and (numeral_difference > next_numeral['value']):
                result += next_numeral['letter'] + numeral['letter']
                remainder -= numeral_difference

        if factor > 0:
            result += numeral['letter'] * factor

    return result

def roman_to_arabic(number):
    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value

    return result

u = True
while u:
    print("Варианты перевода: \n1. Из арабского в римский. \n2. Из римского в арабский.")
    o = int(input("Ответ: "))
    if o == 1:
        i = int(input("Введите число: "))
        print('\nРезультат: ', arabic_to_roman(i))
    elif o == 2:
        i = input("Введите число: ")
        print('\nРезультат: ', roman_to_arabic(i))
    else:
        print("\n\n\n\n\t\t\t\tInvalid input!\n\n\n\n")
        break;
    print("\n\nХотите повторить?(y/n)")
    y = input("Ответ: ")
    if y == 'y':
        u = True
    if y == 'n':
        u = False
        break;
    

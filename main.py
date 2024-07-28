import math
import random


roman_numeral_georgian_map = {
    0: "ნული",
    1: "ერთი",
    2: "ორი",
    3: "სამი",
    4: "ოთხი",
    5: "ხუთი",
    6: "ექვსი",
    7: "შვიდი",
    8: "რვა",
    9: "ცხრა",
    10: "ათი",
    13: "ცამეტი",
    17: "ჩვიდმეტი",
    18: "თვრამეტი",
    19: "ცხრამეტი",
    20: "ოცი",
    100: "ასი",
    1000: "ათასი",
    10**6: "მილიონი",
    10**9: "მილიარდი"
}

georgian_ipa_map = {
    " ": " ",
    "ა": "ä",
    "ბ": "b",
    "გ": "g",
    "დ": "d",
    "ე": "e̞",
    "ვ": "v",
    "ზ": "z",
    "თ": "tʰ",
    "ი": "i",
    "კ": "kʼ",
    "ლ": "l",
    "მ": "m",
    "ნ": "n",
    "ო": "o",
    "პ": "pʼ",
    "ჟ": "ʒ",
    "რ": "ɾ",
    "ს": "s",
    "ტ": "tʼ",
    "უ": "u",
    "ფ": "pʰ",
    "ქ": "kʰ",
    "ღ": "ʁ",
    "ყ": "χʼ",
    "შ": "ʃ",
    "ჩ": "t͡ʃʰ",
    "ც": "t͡sʰ",
    "ძ": "d͡z",
    "წ": "t͡sʼ",
    "ჭ": "t͡ʃʼ",
    "ხ": "χ",
    "ჯ": "d͡ʒ",
    "ჰ": "h"
}

roman_numeral_georgian_numeral_map = {
    1: "ა",
    2: "ბ",
    3: "გ",
    4: "დ",
    5: "ე",
    6: "ვ",
    7: "ზ",
    8: "ჱ",
    9: "თ",
    10: "ი",
    20: "კ",
    30: "ლ",
    40: "მ",
    50: "ნ",
    60: "ჲ",
    70: "ო",
    80: "პ",
    90: "ჟ",
    100: "რ",
    200: "ს",
    300: "ტ",
    400: ["ჳ", "უ"],
    500: "ფ",
    600: "ქ",
    700: "ღ",
    800: "ყ",
    900: "შ",
    1000: "ჩ",
    2000: "ც",
    3000: "ძ",
    4000: "წ",
    5000: "ჭ",
    6000: "ხ",
    7000: "ჴ",
    8000: "ჯ",
    9000: "ჰ",
    10000: "ჵ",
    
}

def stem(str):
    if str[-1] == "ი":
        return str[0:-1]
    return str

def get_digit(num, digit):
    return num // 10**digit % 10

def roman_numeral_to_georgian(num):
    if num in roman_numeral_georgian_map.keys():
        return roman_numeral_georgian_map[num]
    digits = len(str(num))
    if digits == 1:
        return roman_numeral_georgian_map[num]
    elif digits == 2:
        if get_digit(num, 1) == 1:
            return "თ" + stem(roman_numeral_georgian_map[get_digit(num, 0)]) + "მეტი"
        twenties = stem(roman_numeral_georgian_map[num // 20]) + "მ"
        if twenties == "ერთმ":
            twenties = ""
        if twenties == "სამმ":
            twenties = "სამ"
        remainder = "და" + roman_numeral_to_georgian(num % 20)
        if remainder == "დანული":
            remainder = "ი"
        return stem(twenties + roman_numeral_georgian_map[20]) + remainder
    elif digits == 3:
        hundreds = stem(roman_numeral_georgian_map[num // 100])
        remainder = roman_numeral_to_georgian(num % 100)
        if remainder == "ნული":
            return hundreds + roman_numeral_georgian_map[100]
        return stem(hundreds + roman_numeral_georgian_map[100]) + " " + remainder
    else:
        thousands = roman_numeral_to_georgian(num // 1000)
        remainder = roman_numeral_to_georgian(num % 1000)
        if remainder == "ნული":
            return thousands + " " + roman_numeral_georgian_map[1000]
        return stem(thousands + " " + roman_numeral_georgian_map[1000]) + " " + remainder

def georgian_to_ipa(str):
    broad = ""
    for c in str:
        broad += georgian_ipa_map[c]
    narrow = ""
    for i, c in enumerate(broad):
        if c == "l" and broad[i+1] in ["u", "o"]:
            narrow += "ɫ"
        elif c == "v":
            if not (i == 0 or broad[:i].endswith(("ä", "e̞", "i", "o̞", "u", " "))):
                narrow += "ʷ"
            elif broad[i+1:].startswith(("tʰ", "kʼ", "pʼ", "s", "tʼ", "pʰ", "kʰ", "χʼ", "ʃ", "t͡ʃʰ", "t͡sʰ", "t͡sʼ", "t͡ʃʼ", "x", "h")):
                narrow += "f"
            else:
                narrow += c
        elif c in ["b", "d", "g"]:
            if i == 0 or broad[i-1] == " ":
                if c == "b":
                    narrow += "b̥"
                if c == "d":
                    narrow += "d̥"
                if c == "g":
                    narrow += "ɡ̊"
            elif i == len(broad) - 1 or broad[i+1] == " ":
                if c == "b":
                    narrow += "pʰ"
                if c == "d":
                    narrow += "tʰ"
                if c == "g":
                    narrow += "kʰ"
            else:
                narrow += c
        else:
            narrow += c
    return "[{}]".format(narrow)

def roman_numeral_to_georgian_numeral(num):
    digits = [int(d) for d in list(str(num))]
    geo = ""
    for i, digit in enumerate(digits):
        if not digit == 0:
            geo += roman_numeral_georgian_numeral_map[digit * 10**(len(digits) - i - 1)][0]
    return geo

digits = random.randint(1, 6)
number = random.randint(0, 10**digits - 1)

georgian = roman_numeral_to_georgian(number)
print(number)
if number < 20_000:
    print(roman_numeral_to_georgian_numeral(number))
print(georgian)
print(georgian_to_ipa(georgian))
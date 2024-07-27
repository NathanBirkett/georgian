import math
import random


numeral_map = {
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

def stem(str):
    if str[-1] == "ი":
        return str[0:-1]
    return str

def get_digit(num, digit):
    return num // 10**digit % 10

def convert_number(num):
    if num in numeral_map.keys():
        return numeral_map[num]
    digits = len(str(num))
    if digits == 1:
        return numeral_map[num]
    elif digits == 2:
        if get_digit(num, 1) == 1:
            return "თ" + stem(numeral_map[get_digit(num, 0)]) + "მეტი"
        twenties = stem(numeral_map[num // 20]) + "მ"
        if twenties == "ერთმ":
            twenties = ""
        if twenties == "სამმ":
            twenties = "სამ"
        remainder = "და" + convert_number(num % 20)
        if remainder == "დანული":
            remainder = "ი"
        return stem(twenties + numeral_map[20]) + remainder
    elif digits == 3:
        hundreds = stem(numeral_map[num // 100])
        remainder = convert_number(num % 100)
        if remainder == "ნული":
            return hundreds + numeral_map[100]
        return stem(hundreds + numeral_map[100]) + " " + remainder
    else:
        thousands = convert_number(num // 1000)
        remainder = convert_number(num % 1000)
        if remainder == "ნული":
            return thousands + " " + numeral_map[1000]
        return stem(thousands + " " + numeral_map[1000]) + " " + remainder


digits = random.randint(0, 6)
number = random.randint(0, 10**digits - 1)

print(number)
print(convert_number(number))
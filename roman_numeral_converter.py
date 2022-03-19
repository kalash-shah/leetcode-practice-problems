# converts any roman number into its integer format.
I = 1
V = 5
X = 10
L = 50
C = 100 
D = 500
M = 1000
roman_list = []
integer_number = 0

roman_number = input("Enter any roman number: ").upper()
for x in roman_number:
    roman_list.append(x)

char_in_roman_list = len(roman_list)

for num in range(0,char_in_roman_list): # 0,4
    if roman_list[num] == "C":
        if roman_list[num] == "C" and (num != char_in_roman_list-1 and (roman_list[num+1] == "D" or roman_list[num+1] == "M")): 
            integer_number -= C
        else: 
            integer_number += C
    if roman_list[num] == "I":
        if roman_list[num] == "I" and (num != char_in_roman_list-1 and (roman_list[num+1] == "V" or roman_list[num+1] == "X")):
            integer_number -= I
        else: 
            integer_number += I
    if roman_list[num] == "X":
        if roman_list[num] == "X" and (num != char_in_roman_list-1 and (roman_list[num+1] == "L" or roman_list[num+1] == "C")):
            integer_number -= X
        else: 
            integer_number += X
    if roman_list[num] == "V":
        integer_number+= V
    if roman_list[num] == "L":
        integer_number+= L
    if roman_list[num] == "D":
        integer_number+= D
    if roman_list[num] == "M":
        integer_number+= M

print("integer value is: ", integer_number)
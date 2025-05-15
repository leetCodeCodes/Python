roman_algorithms = 'VI'


def roman_to_number_literally(roman_algorithms):
    list_int_roman_algorithms = []
    for i in roman_algorithms:
        if i == "I":
            i = 1
        elif i == "V":
            i = 5
        elif i == "X":
            i = 10
        elif i == "L":
            i = 50
        elif i == "C":
            i = 100
        elif i == "D":
            i = 500
        elif i == "M":
            i = 1000
        list_int_roman_algorithms.append(i)
    return list_int_roman_algorithms


lista_nums = roman_to_number_literally(roman_algorithms)
lista_nums_copy = lista_nums[:]
sum = 0

for i in range(len(lista_nums)):
    if lista_nums[i] < lista_nums[i-1]:
        sum += (lista_nums[i-1] - lista_nums[i])
        lista_nums[i] = 0
    else:
        sum += lista_nums_copy[i]
print(sum)
print(roman_to_number_literally(roman_algorithms))

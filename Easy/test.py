digits = sorted([2, 2, 8, 8, 2])

def findEvenNumbers(digits):
    filtered_digits = []
    list_without_repetition = []
    sorted_digits = sorted(digits)
    for i in range(len(sorted_digits)):
        for n in range(len(sorted_digits)):
            for x in range(len(sorted_digits)):
                if i != n and i != x and n != x: #evita que o mesmo dígito se repita
                    concatenation = f"{sorted_digits[i]}" + f"{sorted_digits[n]}" + f"{sorted_digits[x]}"
                    if sorted_digits[i] != 0:
                        filtered_digits.append(concatenation)
    for i in range(len(filtered_digits)):
        if filtered_digits[i] not in list_without_repetition:
            list_without_repetition.append(filtered_digits[i])

    return [int(list_without_repetition[i]) for i in range(len(list_without_repetition)) if int(list_without_repetition[i][2]) % 2 == 0]


print(findEvenNumbers(digits))

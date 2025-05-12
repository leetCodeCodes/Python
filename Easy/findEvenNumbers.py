digits = sorted([2, 1, 3, 0])


def findEverNumbers(digits):
    filtered_digits = []
    for i in range(len(digits)):
        for n in range(len(digits)):
            for x in range(len(digits)):
                if i != n and i != x and n != x: #evita que o mesmo dígito se repita
                    concatenation = f"{digits[i]}" + f"{digits[n]}" + f"{digits[x]}"
                    if digits[i] != 0:
                        filtered_digits.append(concatenation)
    return [int(digit) for digit in range(len(filtered_digits)) if filtered_digits[digit][2] % 2 == 0]


print(findEverNumbers(digits))

digits = sorted([2, 1, 3, 0])

first_filter = []

for i in range(len(digits)):
    for n in range(len(digits)):
        if i != n: #evita que o mesmo dígito se repita
            first_concatenation = f"{digits[i]}" + f"{digits[n]}"
            if digits[i] != 0:
                first_filter.append(first_concatenation)
print(first_filter)

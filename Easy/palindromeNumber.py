x = 121

def palindromeNumber(x):
    list_x = [digitos for digitos in str(x)]
    opposite_list_x = [list_x[digitos] for digitos in range(len(list_x) - 1, - 1, - 1)]

    if list_x == opposite_list_x:
        return True
    else:
        return False


print(palindromeNumber(x))

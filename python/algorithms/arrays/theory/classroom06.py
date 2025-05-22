#
#
#

# Máximo, mínimo, soma
list_number = [0,45,78,6,32,15]
print(max(list_number))
print(min(list_number))
print(sum(list_number))

mediana_list = [15,48,79,36,56,89,74,15,32]
def mediana(my_list: list):
    ordered = sorted(my_list)
    center_list = len(ordered) // 2
    return ordered[center_list]

print(f"The mediana is: {mediana(mediana_list)}")
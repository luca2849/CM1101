number_of_terms = input("Enter the number of terms to generate > ")
number_of_terms = int(number_of_terms)
def fibbonacci(terms):
    arr = [0, 1]
    output = ""
    for x in range(1, terms):
        arr.append(arr[x] + arr[x-1])
    return arr

array = fibbonacci(number_of_terms)
formatted_array = []
for item in array:
    formatted_array.append(format(item, ",d"))

for item in formatted_array:
    print(item)

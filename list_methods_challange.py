numbers = [3, 3, 5, 7, 2, 5, 7, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

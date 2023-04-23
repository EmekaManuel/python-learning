# for x in range(4):
#     for y in range(3):
#         print(f"{x}, {y}")

# numbers = [5,2,5,2,2]
# for number in numbers:
#     print("x" * number)

# names = ['john', 'peter', 'david', 'mosh']
# print(names[0])

# numbers = [3,6,2,8,4,10]
# numbers.sort()
# print(numbers)

# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]

# print(matrix[0][1])

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)
phone = input("Phone: ")
num_mapping = {
    "1": "one ",
    "2": "two ",
    "3": "three ",
    "4": "four "
}
output = ""
for num in phone:
    output += num_mapping.get(num, "!")
print(output)

 
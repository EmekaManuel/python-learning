# try:
#     age = int(input("age:"))
#     print(age)
# except ValueError :
#     print("Inavlid Error")

try: 
    age = int(input("Age:"))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannt be zero0")
except ValueError:
    print("Invalid Value")
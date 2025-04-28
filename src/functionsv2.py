# def say_hello():
#     print(f"Hello {person}")
#
# def say_bye():
#     print(f"Bye {person}")
#
# def get_person_name():
#     return input("please enter a name of a person: ")
#
# person = get_person_name()
#
# print(f"person name:> {person}")
#
# say_hello()
# say_bye()



num1 = int(input("please enter the 1st number: "))
num2 = int(input("please enter the 2nd number: "))
num3 = int(input("please enter the 3rd number: "))

def sum(num1, num2):
    return num1 + num2

def mult_num3(num3):
    print(num3 * num3)

sum_num = sum(num1, num2)

def add(sum_num, num3):
    result = sum_num + (num3 * num3)
    print(result)

add(sum_num, num3)
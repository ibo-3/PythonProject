print("hello world")

firstname = input("please enter your firstname: ")
lastname = input("please enter your lastname: ")
age = int(input("please enter you age: "))



print (f"My Name is: {firstname}")
print(f"my lastname is: {lastname}")
print(f"my age  is: {age}")

if age > 18:
   print(f"{firstname} {lastname} can be a university student")
   print("second line")
   print("third line")

elif age == 18:
    print(f"{firstname} {lastname} can register to be university student")


else:
    print(f"{firstname} {lastname} is under the age to be student")
    print("try later")


print(type(firstname))
print(type(lastname))
print(type(age))
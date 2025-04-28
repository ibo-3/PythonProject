#1
for num in range(1,11):
    print(num)


#2
for num1 in range(0,20,2):
    print(num1)


#3
world = input("please enter a word: ")
for letter in world:
    print(letter)


#4
num2 = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num2} x {i} = {num2 * i}")


#5
total_sum = 0
for num3 in range(1,101):
    total_sum += num3
    print(f"The sum of numbers from 1 to 100 is: {total_sum}")




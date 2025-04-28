# sum = 0
# for num in range(2,51, 2):
#     sum += num
# print(f"{sum}")
# ##
# numbers = [10, 20, 30, 40, 50]
# total_sum = 0
# for num1 in numbers:
#     total_sum += num1
# average = total_sum / len(numbers)
# print(f"The average is: {average}")

# numbers = [12, 45, 23, 78, 56, 89, 34]
# max_number = numbers[0]
# for num in numbers:
#     if num > max_number:
#         max_number = num
# print(max_number)

# sentence = input("pls enter sentence: ")
# for sen in sentence:
#     print(sen)
#
# word = input("Enter a word: ")
# vowels = "aeiouAEIOU"
# count = 0
# for c in word:
#     if c in vowels:
#         count += 1
# print("The number of vowels:", count)
#
# word = input("Enter a word: ")
# reversed_word = ""
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# print("The reversed word is:", reversed_word)

sentence = input("Please enter a sentence: ").lower()
for letter in sentence:
    if letter == 'a':
        print("Python")

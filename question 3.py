
#   Take a sentence and a word as input and check if the string contains the word in it. Also, count the number of times that word occurs in the string. Do this by using inbuilt string functions and then without using inbuilt string functions

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Word found")
else:
    print("Word not found")

count = sentence.count(word)

print("Number of occurrences =", count)
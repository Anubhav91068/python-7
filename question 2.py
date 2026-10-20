
#Write a program to find the length of the last word in a sentence. 

s = input("Enter a sentence: ")

count = 0
i = len(s) - 1

while i >= 0 and s[i] == " ":
    i = i - 1

while i >= 0 and s[i] != " ":
    count = count + 1
    i = i - 1

print("Length of last word:", count)
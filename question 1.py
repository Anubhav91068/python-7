
#Write a program to reverse a string without using inbuilt function.


s = input("Enter a string: ")

i = len(s) - 1

while i >= 0:
    print(s[i], end="")
    i = i - 1
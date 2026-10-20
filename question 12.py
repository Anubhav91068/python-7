
#Take a sentence as input and remove all the duplicate characters from the string. 

s = input("Enter a sentence: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print("After removing duplicates:", result)
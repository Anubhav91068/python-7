
# A program that takes a string as input and checks where the string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"

s = input("Enter a sentence: ")

s = s.lower()

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in s:
        print("Not a Pangram")
        break
else:
    print("Pangram")
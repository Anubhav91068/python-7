
# Repeatedly take input from the user in the range of 1 – 10 till the time they enter -1. It then displays the histogram shown as follows. Note that the percentage values are displayed till 2 decimal places: 1 - 2: # # # # # # # # # # 52.00 % 3 – 4: # # # # # # 28.00 % 5 – 6: # 4.00 % 7 – 8: 0.00 % 9 – 10: # # # 16 % 

c1 = c2 = c3 = c4 = c5 = 0
total = 0

while True:
    n = int(input("Enter a number (1-10) or -1 to stop: "))

    if n == -1:
        break

    total += 1

    if n == 1 or n == 2:
        c1 += 1
    elif n == 3 or n == 4:
        c2 += 1
    elif n == 5 or n == 6:
        c3 += 1
    elif n == 7 or n == 8:
        c4 += 1
    elif n == 9 or n == 10:
        c5 += 1

print("1-2 :", "#" * c1, f"{(c1/total)*100:.2f}%")
print("3-4 :", "#" * c2, f"{(c2/total)*100:.2f}%")
print("5-6 :", "#" * c3, f"{(c3/total)*100:.2f}%")
print("7-8 :", "#" * c4, f"{(c4/total)*100:.2f}%")
print("9-10:", "#" * c5, f"{(c5/total)*100:.2f}%")
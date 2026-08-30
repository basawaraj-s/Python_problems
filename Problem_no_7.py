list = []
n = int(input("Enter the number "))
for i in range(n+1):
    if i % 2 == 1 and i % 11 != 0 and i % 5 != 0:
            list.append(i)
print(list)
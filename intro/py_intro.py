l = []
n = input("Enter some numbers (q to quit):")
while (n != 'q'):
    l.append(n)
    n = input("Enter the next number (q to quit):")
l.sort()
for i in l:
    print(i)
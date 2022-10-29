#While loop
a = 1

while a < 10:
    print(a)
    a = a + 1

a = 1
while a < 10:
    a = a + 1

    if a == 5:
        continue
    print(a)


a = 1
while a < 10:
    a = a + 1

    if a == 5:
        break
    print(a)

#in

quote = "A quick brown fox jumps over the lazy dog"

if "quick" in quote:
    print("Yes")
else:
    print("No") 

a = "Hello World"
print(a[:8])

a = "IT'S NOTHING"

print(a.upper())
print (a.lower())
print(a.strip())
print(a.replace("H", "Y"))
print(a.replace("IT'S" , " "))

print("This is an example of slash n \n Hello there \n Namasteyyy")

#take a string of length 5 [index 0-4]
#print first char
#print middle char
#print last char

a = "Files"
print(a[0])
print(a[2])
print(a[4])
b = len(a)
print(b)
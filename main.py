# ex. 1
print("ex. 1")
price = {"apple" : 10, "milk" : 12, "bread" : 5}
mylist = [("apple", 2), ("milk", 2)]

list1 = [price.get(e[0]) * e[1] for e in mylist]
sum1 = sum(list1)
print(sum1, "\n")

# ex. 2
print("ex. 2")
friends = [("andrew", 10), ("george", 20), ("andrew", 5), ("ann", 10)]
set2 = set([e[0] for e in friends])
print(set2, "\n")

# ex. 3
print("ex. 3")
number = int(input("Enter a number: "))
pow3 = 1
if number % 2 == 1: pow3 = 2
for i in range(number + 1):
    print(i ** pow3)
print("\n")

# ex. 4
print("ex. 4")
s_in = "abcdefghijklmnop"
num_in = int(input("Enter a number: "))
dict1 = {}
if num_in < len(s_in):
    for i in range(num_in):
        dict1[i] = s_in[i]
else:
    print("Invalid Input")
print(dict1, "\n")

# ex. 5
print("ex. 5")
def compute_string(strp1):
    strp2 = ""
    for i in strp1:
        strp2 += chr(ord(i) + 1)
    return strp2

str1 = "abcdefghijklmnop"
str2 = compute_string(str1)
print(str2, "\n")

# ex. 6
print("ex. 6")
f1 = open(r"file1.txt")
f2 = open("file2.txt", "w")

line = f1.readline()
while line:
    list6 = line.split(" ")
    list6 = [e[0].upper() + e[1:] for e in list6]
    f2.writelines(" ".join(list6))
    line = f1.readline()

f1.close()
f2.close()



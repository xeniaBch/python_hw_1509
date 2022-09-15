# Level 1
# Task1
st0 = input("Enter string 0 ")
k = 0
for i in st0[1:]:
    if i == st0[0]:
        k += 1
print(k)

# Task2
st1 = input("Enter string 1 ")
for i in st1:
    print(i)

# Task3
st2 = input("Enter string 2 ")
k = 0
tmp = st2[1:len(st2):2]
for i in tmp:
    if i == 'y':
        k += 1
print(k)

# Level 2
# Task1
st3 = input("Enter string 3 ")
if len(st3) % 2 != 0:
    print(st3[0:len(st3) // 2] + st3[(len(st3) // 2) + 1:])
else:
    print('odd string')

# Task2
st4 = input("Enter string 4 ")
k = 0
for i in st4:
    if i.isdigit():
        k += 1
print(k)

# Task3
txt = "Hello! My name is Xenia. And your? I am your student."
print("There are", txt.count(".") + txt.count("!") + txt.count("?"), "sentences")


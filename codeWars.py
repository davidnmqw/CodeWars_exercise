t1 = "mnooopqrsttt"
t2 = "xyzzzzabc"
# def lngs(t1, t2):
#     a, t = "", t1 + t2
#     for i in t:
#         if i not in a:
#             a += i
#     return "".join(sorted(a))
# print(lngs(t1, t2))

def lngs(t1, t2):
    return "".join(sorted(set(t1 + t2)))             #úprava s gpt
print(lngs(t1, t2))

import random       #telefonní čílo generátor
r = list(range(10))
s, s1, s2 = "".join(map(str, random.choices(r, k=3))), "".join(map(str, random.choices(r, k=3))), "".join(map(str, random.choices(r, k=4)))
s1 = "".join(map(str, random.choices(r, k=3)))
s2 = "".join(map(str, random.choices(r, k=4)))
print(f"{s} {s1}-{s2}")

#growth of a population
p = 1000
per = 0.02
income = 50
year = 0
while p <= 1200: p += p * per + income; year += 1
print(year)

#two numbers
a = list(range(13,50))
b = 64
def two_sum(numbers, target):
    pass
print(two_sum(a, b))

#break camelCase
s = "different ThingLittleTry"
t, z, = "", " "
for idx, i in enumerate(s):     #klíčem bylo použít funkci enumerate 
    if i == i.upper() and i != " " and z != " ":
        t += s[:idx] + " "      #zaítm nefunguje
        s = s[idx:]
    z = i
t += s
print(" ".join(t.split()))

#další pokus, s využitím původního s beze změny
s = "different ThingLittleTry"
t, z, f = "", " ", 0
for idx, i in enumerate(s):     #klíčem bylo použít funkci enumerate 
    if i == i.upper() and i != " " and z != " ":
        t += s[f:idx] + " "      #logiku jsem vymyslel sám
        f = idx                 #gpt to nezvládl vylepšit
    z = i
t += s[f:]
print(" ".join(t.split()))

print("podle CodeWars")
s = "different Thing   LittleTry"
print("".join([" " + c if c.isupper() else c.replace(" ","") if c == " " else c for c in s]))

a = [1, 0, 1, 2, 0, 1, 3]
for i in a:
    if i == 0:
        a.append(i)             #moje logika
        a.remove(i)
print(a)

def zero(a):
    return [i for i in a if i != 0] + [i for i in a if i == 0]
a = [1, 0, 1, 2, 0, 1, 3]       #úprava gpt na jeden řádek
print(zero(a))

def zero(a):
    return [x for x in a if x] + [0]*a.count(0)
a = [1, 0, 1, 2, 0, 1, 3]           #podle codewars
print(zero(a))

#Roman numeral translator
#num = reversed(str(15))      #MCMLXV
#roman = {"1":"I", "5":"V", "10":"X", "50":"L", "100":"C", "500":"D", "1000":"M"}
#fin = []
#for i in num:
#    a = 6
#    fin.append(roman[i])       neumím to vyřešit
#    print(roman.index(i))
#    #roman = roman[roman.index(i):]
#print("".join(fin))

#multiples 3 or 5
num = 200
i = total = 0
while i < num:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1
print(total)

    #better with gpt
num = 200
print(sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0))

#move first letter to end of the word and add "ay" other unchanged
import string
    #druhý pokus, už funkční
text = "Pig, wurst !".split()
c, newt = 0, ""
for word in text:
    for letter in word:
        if any(letter in string.punctuation for letter in word) and len(word) > 1:
            word = word[1:len(word)-1] + word[0] + "ay" + word[-1]
            newt += word + " "
            break
        elif letter in string.punctuation:
            newt += word + " "
            break
        elif all(letter not in string.punctuation for letter in word):
            word = word[1:len(word)] + word[0] + "ay"
            newt += word + " "
            break
print(newt.strip())
    #třetí pokus - zkrácení
text = "Pig, wurst and !".split()
result = []
for word in text:       #with help of gpt
    if word in string.punctuation:
        result.append(word)
    elif any(i in string.punctuation for i in word):
        result.append(word[1:len(word)-1] + word[0] + "ay" + word[-1])
    elif all(i not in string.punctuation for i in word):
        result.append(word[1:len(word)] + word[0] + "ay")
print(" ".join(result))
    #codeWars
text = "Pig wurst and !"    #když je interpunkce hned za slovem tak nefunguje
print(" ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split()))

#rgb to hexadecimal
r = -255
g = 24
b = 0
podmínka = lambda x: 0 if x < 0 else 255 if x > 255 else x
r, g, b = podmínka(r), podmínka(g), podmínka(b)
print(format(r, "02X") + format(g, "02X") + format(b, "02X"))

import time
#direction reduction
# def dir_reduc(arr):
#     dic = {
#         "NORTH" : "SOUTH",
#         "EAST" : "WEST",
#         "SOUTH" : "NORTH",
#         "WEST" : "EAST"
#     }   #použít while loop při manipulaci prvků
#     for idx, i in enumerate(arr[:-1]):
#         a, b = i, dic[arr[idx + 1]]
#         if a == b:
#             arr.remove(arr[idx])
#             arr.remove(arr[idx])
#             arr = arr
#     print(arr)
# arr = ["NORTH", "SOUTH", "EAST", "EAST", "WEST", "NORTH", "WEST"]
#dir_reduc(arr)
    #druhý pokus - OK
start = time.time()
def dir_reduc(arr):
    dic = {
        "NORTH" : "SOUTH",
        "EAST" : "WEST",
        "SOUTH" : "NORTH",
        "WEST" : "EAST"
    }
    idx = 0
    while idx < len(arr[:-1]):
        if arr[idx] == dic[arr[idx + 1]]:
            arr.pop(idx); arr.pop(idx); idx = 0
            continue
        idx += 1
    return arr
arr = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"]
print(dir_reduc(arr)) #["NORTH", "EAST"]
end = time.time()
print(f"David trval: {end - start} sekund")

    #verze GPT
start = time.time()
def dir_reduc_gpt(arr):
    dic = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}
    stack = []
    for direction in arr:
        if stack and stack[-1] == dic[direction]:
            stack.pop()
        else:
            stack.append(direction)
    print(stack)
arr = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"]
dir_reduc_gpt(arr)
end = time.time()
print(f"GPT trval: {end - start} sekund")

#next bigger number with same digit
# n = a = 21385048424
# citer = lambda x: [int(i) for i in str(x)]  #convert to iterable
# cnum = lambda x: int("".join(map(str, x)))  #convert to number
# a = citer(a)
# n = citer(n)
# while cnum(sorted(n, reverse=True)) > cnum(a):
#     a = cnum(a) + 1
#     a = citer(a)
#     if sorted(a) == sorted(n):
#         print(cnum(a))
#         quit()
# print(-1)
    #druhý pokus
import time
start = time.time()
def nextf(n):
    citer = lambda x: [i for i in str(x)]  #odebral jsem int(i)
    cnum = lambda x: int("".join(x))  #odebral jsem map(str, x)
    a = n = citer(n)                #zkusit přes timeit porovnat rychlost kódu
    while cnum(sorted(n, reverse=True)) > cnum(a):
        a = cnum(a) + 1
        a = citer(a)        #->trvá moc dlouho!!!
        if sorted(a) == sorted(n):
            return cnum(a)
            quit()
    return -1
print(nextf(85397755))
end = time.time()
print(f"trvalo to: {end - start} sekund")

from line_profiler import LineProfiler
profiler = LineProfiler()
profiler.add_function(nextf)
profiler_wrapper = profiler(nextf)
result = profiler_wrapper(8539775)
#profiler.print_stats()
    #třetí pokus
start = time.time()
def nextf(n):
    citer = lambda x: [int(i) for i in str(x)]  #odebral jsem int(i)
    cnum = lambda x: int("".join(map(str,x)))  #odebral jsem map(str, x)
    a = n = citer(n)                #zkusit přes timeit porovnat rychlost kódu
    while cnum(sorted(n, reverse=True)) > cnum(a):
        a = list(reversed(a))
        for idx, i in enumerate((a)):
            if i != 9:
                a[idx] += 1
                break
            else:
                if idx + 1 == len(a):
                    a.append(1)
                    a[-2] = 0
                    break
                else:
                    a[idx] = 0
        a = list(reversed(a))
        if sorted(a) == sorted(n):
            return cnum(a)
            quit()
    return -1
print(nextf(85397755))
end = time.time()
print(f"trvalo to: {end - start} sekund")

a = list(reversed([2,1,9]))
for idx, i in enumerate((a)):
    if i != 9:
        a[idx] += 1
        break
    else:
        if idx + 1 == len(a):
            a.append(1)
            a[-2] = 0
            break
        else:
            a[idx] = 0
print(list(reversed(a)))
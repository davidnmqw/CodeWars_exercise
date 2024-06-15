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

#for i in s:
#    if i == i.upper() and i != " " and s[s.index(i) - 1] != " ":
#        t += s[:s.index(i)] + " "
#        s = s[s.index(i):]
#t += s
#print(t)

#z = " "
#for i in s:
#    if i == i.upper() and i != " " and z != " ":
#        t += s[:s.index(i)] + " "
#        s = s[s.index(i):]
#    z = i
#t += s
#print(" ".join(t.split()))
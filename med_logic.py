#1. kontrola anagramu
a = "reklama"
b = "makrela"
def anag(a, b):
    a, b = sorted(a), sorted(b)
    if a == b:
        return True
    else:
        return False
print(anag(a,b))

#2. funkce vrátí min a max
import statistics
a = [1, 4, -20, 57, 3250, -480, 120, 43, -3]
def minmax(a):
    mini, maxi = min(a), max(a)
    rez = (mini, maxi)
    menidan = statistics.median(a)
    print(f" minimum ({mini}) a maximum ({maxi}) jsou: {rez} a medián: {menidan}")
minmax(a)

#3. závorka balancer, druhý pokus, funguje pouze pokud jsou závorky symetrické v textu a ne když se ocitnou samostatně
print("3. závorky, druhý pokus:")
text = "Ahoj, {tohle [a navíc, i jiné(aktivní věci) mohou fungovat]}"
a = []
b = []
def is_balanced(text):
    for i in text:
        if i == "(" or i == "[" or i == "{":
            a.append(i)
    b_map = {")" : "(", "]" : "[", "}" : "{"}
    for i in text:
        if i in b_map:              # Tohle je kód GPT s použitím slovníku b_map
            b.insert(0, b_map[i])
    # for i in text:
        # if i == ")" or i == "]" or i == "}":
        #     if i == ")":
        #         i = "("
        #         b.insert(0, i)        # Tohle je můj postup
        #     elif i == "]":
        #         i = "["
        #         b.insert(0, i)
        #     else:
        #         i = "{"
        #         b.insert(0, i)
    if a == b:
        print(True)
    else:
        print(False)
is_balanced(text)

#3. závarky univerzální použití
# print("3. závarky univerzální použití")
# text = "(Ahoj), {tohle [a navíc, i jiné(aktivní věci) mohou fungovat]}"
# a = []
# for i in text:
#     if i == "(" or i == "[" or i == "{" or i == ")" or i == "]" or i == "}":
#         a.append(i)
# slovnik = {"(":")" , "[":"]" , "{":"}"}
# for i in a:
#     if i in slovnik:        #nevím jak dál, zkusit dodělat

#3. závorky uni 3. pokus
print("3. závarky univerzální použití")
text = "Začá[]te{k je (Ahoj)}, {tohle [a navíc, i jiné(aktivní věci) mohou fungovat]}"
slovnik = {"(":")" , "[":"]" , "{":"}"}
a, x, y = [], 0, 0
for i in text:
    if i == "(" or i == "[" or i == "{":
        tex = text[text.index(i) + 1:]
        for j in tex:
            if j == slovnik[i]:         #vyřešil jsem výhradně sám
                a.append(True)
                break
x = sum(1 for i in text if i in slovnik.keys())
y = sum(1 for i in text if i in slovnik.values())
if x == y:
    print(len(a) == x)
else:
    print(False)
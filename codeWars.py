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
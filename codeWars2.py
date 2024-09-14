#next bigger number
# od začátku, pouze manipulace pole
import time
start = time.time()
def next_begger(n):
    n = [int(i) for i in str(n)]# původní které navyšuji
    max = sorted(n, reverse=True) # největší číslo
    if max == n:
        print(n)
        quit()
    else:
        n[-1] += 1
    def same(max, n):
        return max == sorted(n, reverse=True)
    while not same(max, n):
        n = list(reversed(n))
        for idy, j in enumerate((n)):   #přište jedničku k itterable
            if j != 9:
                n[idy] += 1
                break
            else:
                if idy + 1 == len(n):
                    n.append(1)
                    n[-2] = 0
                    break
                else:
                    n[idy] = 0
        n = list(reversed(n))
    return n
next_begger(853977)
end = time.time()
print(f"david trvalo to: {end - start} sekund")

# from line_profiler import LineProfiler
# profiler = LineProfiler()
# profiler.add_function(next_begger)
# profiler_wrapper = profiler(next_begger)
# result = profiler_wrapper(8539771472386)
# profiler.print_stats()

morse = ".- -.-. -..   -.-. -..   -.-. -.. .- ." # acd cd cdae
mcdic = {
    ".-" : "a",
    "-..." : "b",
    "-.-." : "c",
    "-.." : "d",
    "." : "e",
}
def mctrans(text):
    print([mcdic[i] for i in text.split(" ") if i != ""])
mctrans(morse)
#print([key for key in mcdic.keys()][1])
text = "dav"
for i in text:
    print(list(mcdic.keys())[list(mcdic.values()).index(i)] if i in mcdic.values() else None)
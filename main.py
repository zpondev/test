a = [61, 228, 9, 0, 97, 97]
print(sum(a))

def rec(sp):
    if len(sp) == 0:
        return 0
    return sp.pop() + rec(sp)

print(rec(a))

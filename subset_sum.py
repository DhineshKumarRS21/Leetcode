sub = [2, 3, 7]
tar = 11
n = len(sub)
def recur(ind, t):
    if t == 0:
        return True
    if ind == n:
        return
    if recur(ind + 1, t - sub[ind]):
        return True
    if recur(ind + 1, t):
        return True
    return False
print(recur(0, tar))

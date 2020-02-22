# # #  # https://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
from random import shuffle

st = """ا 1
ب 2
ج 3
د 4
ه‍ 5
و 6
ز 7
ح 8
ط 9
ی 10
ک 20
ل 30
م 40
ن 50
س 60
ع 70
ف 80
ص 90
ق 100
ر 200
ش 300
ت 400
ث 500
خ 600
ذ 700
ض 800
ظ 900
غ 1000"""






def f(v, i, S, memo):
    if i >= len(v): return 1 if S == 0 else 0
    if (i, S) not in memo:  # <-- Check if value has not been calculated.
        count = f(v, i + 1, S, memo)
        count += f(v, i + 1, S - v[i], memo)
        memo[(i, S)] = count  # <-- Memoize calculated result.
    return memo[(i, S)]

def g(v, S, memo):
    subset = []
    for i, x in enumerate(v):
        # Check if there is still a solution if we include v[i]
        if f(v, i + 1, S - x, memo) > 0:
            subset.append(x)
        S -= x
    return subset

memo = dict()
v = [1, 2, 3, 10]
suma = 116










nums = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]
letters = ['ا','ب','ج','د','ه','و','ز','ح','ط','ی','ک','ل','م','ن','س','ع','ف','ص','ق']


num = 121

si = [[6], [1,5], [1,2,3], [2,4],[1,1,2,2], [3,3]]
ti = [[20,30,60]]

res = []




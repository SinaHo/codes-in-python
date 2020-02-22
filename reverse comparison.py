def reverse_comparison(a,b):
    x = int(''.join(list(str(b))[::-1]))
    y = int(''.join(list(str(a))[::-1]))
    if x < y :
        return "{} < {}".format(b,a)
    elif x > y:
        return "{} < {}".format(a,b)
    return "{} = {}".format(a,b)
import sys

print(reverse_comparison(18,25))
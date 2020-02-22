"""
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))

for x in it:
    print(x)

print("end")

import sys
while True:
    try:
        print(next(it))
    except StopIteration as e:
        print(str(e))
        """

import sys 
def fib(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a 
        a, b = b, a + b
        counter += 1 
f = fib(5)
while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(str(e))
        sys.exit()

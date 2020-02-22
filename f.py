def reverseParentheses(s):
    def par(a):
        #Returns content of outermost paranthesses
        if '(' in a:
            return a[a.index('(') + 1:len(a) - a[::-1].index(')')-1]
        return 0
    def pa(a):
        #Returns content of innermost paranthesses
        if '(' in a:
            return a[len(a) - a[::-1].index('('):a.index(')')]
        return 0
    def rev(a):
        temp = a
        while temp:
            p = pa(a)
            if p:
                temp = p
            else:
                break
            a = a.replace('(' + temp + ')', temp[::-1])
            if '(' not in a:
                return a

def eul21():
    def sum_divs(n):
        s = 0
        for i in range(1,n):
            if not n % i:
                s += i 
        return s
    print(sum_divs(220))
    return 0
    s = 0
    for i in range(1,10001):
        if sum_divs(i) == sum_divs(sum_divs(i)):
            s += i 
    print(s)
    return s

eul21()
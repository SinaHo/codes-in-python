
def take_apart(length):
    def triangle_inequ(l):
        return max(l)<sum(l)-l.pop(l.index(max(l)))
    def clean_set(lis):
        out=[]
        for item in lis:
            if item not in out:
                out.append(item)
        return out

    lengths = []
    for i in range(1,length//2+2):
        for j in range(1,length-i+1):
            s = [i,j,length-i-j]
            if triangle_inequ(s):
                s.sort()
                lengths.append(s)
    
    l = clean_set(lengths)
    return len(l)

print(take_apart(12))

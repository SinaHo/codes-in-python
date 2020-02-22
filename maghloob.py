num = float(input("Enter number\n"))
intPart = num - (num % 1)
tmpInt = intPart
tmp = num
while int(tmp) != tmp:
    tmp *= 10
    tmpInt *= 10
floatPart = int(tmp - tmpInt) 
print(floatPart)
def reverse(num):
    ret = 0
    while num  >= 1:
        ret *= 10
        ret += num % 10
        num //= 10
    return ret
floatPart = reverse(floatPart)
intPart = reverse(intPart)
while intPart >=1:
    intPart /= 10
print(str(floatPart + intPart))


def get_len(number):
    n = 0
    while number >= 1:
        n += 1
        number /= 10
    return n - 1


def cut(number):
    if get_len(number) == 0:
        return [number] * 3
    right = number % 10
    left = (number - number % (10 ** get_len(number))) / (10 ** get_len(number))
    number -= left * (10 ** get_len(number))
    number = (number - right) / 10
    return [int(number), int(left), int(right)]


def first():
    number = int(input("enter your number\n"))
    bol = True
    l = get_len(number)
    for i in range((get_len(number) + 1)//2 + 1):
        c = cut(number)
        if c[1] != c[2]:
            print("not palindrome")
            bol = False
            break
    number = c[0]
    if bol:
        print("palindrome")

def second():
    number = int(input("enter your number\n"))
    temp = number
    rev = 0
    while number >= 1:
        rev *= 10
        rev += number % 10
        number //= 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")
    
if __name__ == "__main__":
    #first()
    second()





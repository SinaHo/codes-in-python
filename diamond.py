n = int(input("enter\n"))
j = 2
k = n-2
for i in range(n//2):
    # temp=(n-2*i)//2
    # print(temp)
    if i == 0:
        print(n*'*')
    elif i > 0:
        temp = (n-2*i)//2
        # print(temp)
        print(temp*'*'+' '*j+temp*'*')
        j += 2
for t in range(n//2):
    if t == 0:
        print('*'+' '*k+'*')
        k -= 2
    elif t > 0:
        temp = t+1
        print('*'*temp+' '*k+'*'*temp)
        k -= 2

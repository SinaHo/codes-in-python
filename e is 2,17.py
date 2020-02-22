import time
n=1
while True:
    if 0<n<20:
        print("n = ",n,"   ",str((1+1/n)**n)+"\n_____________\n")
        n+=1
    elif 19<n<200000:
        print("n = ",n,"   ",str((1+1/n)**n)+"\n_____________\n")
        n+=100
    else:
        print("n = ",n,"   ",str((1+1/n)**n)+"\n_____________\n")
        n+=100000000000
    time.sleep(0.5)


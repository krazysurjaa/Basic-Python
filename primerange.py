def primerange(start,end):
    for i in range(start,end+1):
        ctr=0
        for j in range(2,i):
            if i%j==0:
                ctr=ctr+1
        if ctr==0:
            print(i)

m = int(input('enter start : '))
n = int(input('enter end : '))
primerange(start,end)

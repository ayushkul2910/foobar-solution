def divide(num,count):
    while True:
        if(num%2==0):
            num=num/2
            count+=1
        else:
            break


    return num,count



num=int(raw_input())
count=0
a,count=divide(num,count)
while(a!=1):
    a,count=divide(a,count)
    if(a==3):
        count+=2
        a=1
    elif(a!=1):
        b=a+1
        c=a-1
        count+=1
        if(b%4==0):
            b=b/4
            a=b
            count+=2
        else:
            c=c/4
            a=c
            count+=2
        

print(count)














def answer(string):
    sum1=0
    for i in range(0,len(string)):
        count=0
        if string[i]==">":
            for x in range(i,len(string)):
                if string[x]=="<":
                    count+=1
            sum1+=count

    return sum1*2



string=raw_input()
result=answer(string)
print(result)

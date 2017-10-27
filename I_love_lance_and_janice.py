

def answer(string):
    l=[]
    for i in string:
        if ord(i) in range(97,124):
            k=ord(i)
            k=219-k
            l.append(chr(k))
        else:
            l.append(i)

    return ''.join(l)
                   

string=raw_input()
result=answer(string)
print(result)

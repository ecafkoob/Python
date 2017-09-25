def to_weird_case(string):
    arr=string.split()
    count=0
    for i in arr:
        tmp=list(i)
        for j in range(len(tmp)):
            if j%2==0:
                tmp[j]=tmp[j].upper()
        arr[count] = ''.join(tmp)
        count+=1
    return ' '.join(arr)


'''
一个比较不错的版本

def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])
    
'''
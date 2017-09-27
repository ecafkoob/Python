def pig_it(text):
    l=text.split()
    count=0
    for i in l:
        if i.isalpha():
            tmp=list(i)
            tmp.append(tmp[0])
            tmp.pop(0)
            tmp.extend(list('ay'))
            l[count]=''.join(tmp)
        count+=1

    return ' '.join(l)

'''
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''
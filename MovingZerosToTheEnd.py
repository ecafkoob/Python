def move_zeros(array):
    l=[i for i in array if i!=0 or str(i)=='False']
    t=array.count(0)
    for i in range(t):
        l.append(0)
    for i in range(len(l)-len(array)):
        l.pop()
    return l

'''
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
'''
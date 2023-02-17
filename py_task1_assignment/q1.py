import math
def prod(l):
    li=[]
    for i in l:
        l1,l2,l3=[],[],[]
        if type(i)==int:
            li.append(i)
        elif type(i)==list or type(i)==tuple or type(i)==set:
            l1=[j for j in i if type(j)==int]
        
        elif type(i)==dict:
            l2=[k for k in i.keys() if type(k)==int]
            l3=[v for v in i.values() if type(v)==int]
        li+=l1+l2+l3
            
    return math.prod(li)

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
print(prod(list1))
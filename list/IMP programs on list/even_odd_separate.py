
def separator(l):
    even = [x for x in l if x%2==0]
    odd = [x for x in l if x%2!=0]
    return even,odd

li = [1,2,3,4,5,6,7,8,9,10]
even,odd=separator(li)
print(even,odd)
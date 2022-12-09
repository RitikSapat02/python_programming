#_____________WRONG WAY________________:
# li = [1,2,3,4,5,6]
# li1=li
# li1.clear()
# print(li)             #empty


#_______________CORRECT WAYS____________:

#COPY FUNCTION
# LI = [1,2,3,4,5,6]
# li = LI.copy()
# print(li,LI)
# li.clear()
# print(li,LI)

#LIST CONSTRUCTOR
# LI = [1,2,3,4,5,6]
# li = list(LI)
# print(li,LI)
# li.clear()
# print(li,LI)

#list slicing
# li = [1,2,3,4,5,6]
# l = li[:]
# print(l)
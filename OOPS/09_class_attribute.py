class examination_room:
    #class attributes
    classteacher = "kamla"
    totalstudents = 20

a = examination_room()
b = examination_room()

a.subject = "maths"    #instance attricute

examination_room.roomId = 22     #class atribute

print(examination_room.roomId)
print(a.__dict__)        #only instance attribute
print(b.__dict__)

print(examination_room.__dict__)      #class dictionary

#acessing clas attribute using object
print(a.classteacher)


#updating using classname
examination_room.classteacher = "Manisha"
print(a.classteacher)
print(b.classteacher)
print(examination_room.classteacher)

#updating using object
a.totalstudents = 50    #now becomes instance attribute
print(a.totalstudents)          
print(b.totalstudents)
print(examination_room.totalstudents)
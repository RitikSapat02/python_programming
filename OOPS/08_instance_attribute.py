class student_awards:
    pass

aman = student_awards()
nikhil = student_awards()
sahil = student_awards()

#each object with a diffrent instance attributes
aman.game = "chess"
aman.price = "gold"
aman.scholarship = "5k"

nikhil.contest = "dance"
nikhil.internship = "google"
nikhil.cash = "10k"

sahil.award = "first-runner-up"
sahil.fees_return = "4k"

#printing instance attributes
print(aman.__dict__)
print(nikhil.__dict__)
print(sahil.__dict__)


#'''inbuild functions'''

#hasattr(obj , attribute)
print(hasattr(aman,"contest"))
print(hasattr(nikhil,"cash"))
print(hasattr(sahil,"award"))

#setattr(obj,attr,val)

setattr(aman,"coding",False)
setattr(nikhil,"coding",True)
setattr(sahil,"coding",True)

print(aman.__dict__, nikhil.__dict__,sahil.__dict__)


#delattr(obj,attr)
delattr(aman,"coding")
delattr(nikhil,"coding")
delattr(sahil,"coding")
print(aman.__dict__, nikhil.__dict__,sahil.__dict__)

#getattr(obj,attr,optional (def_value))
print(getattr(aman,"price","not there"))
print(getattr(nikhil,"cash","not there"))
print(getattr(sahil,"coding","not there"))

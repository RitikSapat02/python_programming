class student:
    def __init__(self,name,rollNo,branch,reg_id = "NA"):
        self.name = name
        self.roolNo= rollNo
        self.branch = branch
        self.reg_id=reg_id
    
s1=student("Ritik",54,"CSE",2020)
s2=student("Rahu",47,"AI")

print(s1.__dict__)
print(s2.__dict__)


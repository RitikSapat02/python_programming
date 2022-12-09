class RailwayForm :
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harry = RailwayForm()
harry.name = "harry"
harry.train = "Rajdhani Express"
harry.printData()
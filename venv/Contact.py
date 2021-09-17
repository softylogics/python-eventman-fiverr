class Contact:
    
    #contructor
    def __init__(self, name, tNumber):
        self.name = name
        self.tNumber = tNumber

    #toString method
    def toString(self):
        print("Name : ", self.name, ", Telephone number = ", self.tNumber)

    #getter
    def getName(self):
        return self.name

    #getter
    def getPhone(self):
        return self.tNumber

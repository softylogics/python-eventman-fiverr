from Contact import Contact

#parent class for classes Appointment , Meeting 
class Event:
    
    #constructor
    def __init__(self, name, tNumber, startDateTime):
        self.contact = Contact(name, tNumber) #creating Contact class object as attribute
        self.startDateTime = startDateTime
        
    #abstract method
    def getDate(self):
        pass

    #toString method
    def toString(self):
        self.contact.toString()
        print("Event Date : ", self.startDateTime)



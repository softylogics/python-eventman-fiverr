from Event import Event
from datetime import datetime

class Appointment(Event):

    #constructor
    def __init__(self, name, tNumber, startDateTime, appointmentType):
        self.appointmentType = appointmentType 
        Event.__init__(self, name, tNumber, startDateTime) #super class constructor
    
    #toString method
    def toString(self):
        super().toString() # prints contact info and date/time
        print("Appointment Type : ", self.appointmentType) 
    
    #getter
    def getAppointmentType(self):
        return appointmentType

    #getter
    def getDate(self):
        return self.startDateTime.date()






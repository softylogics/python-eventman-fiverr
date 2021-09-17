from Event import Event


class Meeting(Event):

    #constructor
    def __init__(self, name, tNumber, startDateTime, attendees):
        self.attendees = attendees
        Event.__init__(self,name, tNumber, startDateTime) #calling super class constructor

    #toString method
    def toString(self):
        super().toString() #prints contact info and date/time
        print("\nAttendees are as follows:")
        for attendee in self.attendees:
           print(attendee)

    #this method adds attendee for the meeting event
    def addAttendee(self, name):
        self.attendees.append(name)

    #getter
    def getAttendees(self):
        return self.attendees

    #getter
    def getDate(self):
        return self.startDateTime.date()
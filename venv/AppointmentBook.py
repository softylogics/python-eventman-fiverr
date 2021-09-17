from Event import Event
from Meeting import Meeting
from Appointment import Appointment
from datetime import datetime


class AppointmentBook:

    #contsructor
    def __init__(self):
        self.listOfEvents: Event = []

    #when user selects 1 at the main menu, this method is called to add an event
    def addEvent(self):

        #menu to select the type of event
        print("\n1: Meeting\n2: Appointment")
        userInput = input("\nEnter the type of event you want to add: ")


        if userInput == '1': #code region for adding a meeting

            #take input from user the required attributes for creating a Meeting object
            name = input("Enter name of the person: ")
            tNumber = input("Enter Telephone Number of the person: ")
            dateTime = input("Enter date/time for the meeting (dd-mm-yyyy hh:mm): ")
            try:
                date_obj = datetime.strptime(dateTime, '%d-%m-%Y %H:%M')
            except ValueError:
                print('Please input correct date/time format')
                exit()
            except:
                print("An exception occurredd")
                exit()
            attendee = ''
            attendees = [] #attendees list
            attendeeCounter = 1

            #adds attendees untill user presses 'q'
            while attendee != 'q':
                attendee = input(f"Enter attendee {attendeeCounter} name (enter 'q' to finish entering attendees names): ")
                if attendee!= 'q':
                    attendees.append(attendee)
                    attendeeCounter = attendeeCounter + 1



            #this if statement checks if anyother events are registered at the same date
            if len(self.getEventForDate(date_obj)) > 0:
                eventCounter = 0
                canAdd = True;

                #this loop iterates through the events on the same date to check conflict of same time
                for event in self.getEventForDate(date_obj):
                    eventCounter += 1
                    # creating temporary Date Object from event object to use for comparison
                    tempDateObj = event.startDateTime

                    #creating upper bound for comparison
                    tempDateObjMaxBound = tempDateObj.time().replace(minute=tempDateObj.time().minute + 59)

                    #creating lower bound for comparison
                    tempDateObjMinBound = tempDateObj.time().replace(hour=tempDateObj.time().hour - 1, minute=date_obj.time().minute + 1)

                    #comparing both bounds with the user's input event date
                    if date_obj.time() > tempDateObjMaxBound or date_obj.time() < tempDateObjMinBound:
                        print('No conflict found for event {eventCounter}')
                    else: #if conflict found, mark canAdd boolean as false
                        canAdd = False
                        print(f'Conflict Found with {tempDateObj}')

                #simple boolean comparison to add or not add an event
                if canAdd:
                    print("Event cannot be added. Timing already booked")
                else:
                    event = Meeting(name, tNumber, date_obj, attendees)
                    self.listOfEvents.append(event)
                    print("\nEvent added")

            #if no events are found on the same date, just add the event
            else:
                event = Meeting(name, tNumber, date_obj, attendees)
                self.listOfEvents.append(event)
                print("\nEvent added")

        #if user selects to add appointment
        elif userInput == '2':

            # take input from user the required attributes for creating a Meeting object
            name = input("Enter name of the person: ")
            tNumber = input("Enter Telephone Number of the person: ")
            dateTime = input("Enter date/time for the meeting (dd-mm-yyyy hh:mm): ")
            appointmentType = input("Enter appointment type: ")

            #creating datetime object from user input
            try:
                date_obj = datetime.strptime(dateTime, '%d-%m-%Y %H:%M')
            except ValueError:
                print('Please input correct date/time format')
                exit()
            except:
                print("An exception occurredd")
                exit()
            # this if statement checks if anyother events are registered at the same date
            if len(self.getEventForDate(date_obj)) > 0:
                eventCounter = 0
                canAdd = True;

                # this loop iterates through the events on the same date to check conflict of same time
                for event in self.getEventForDate(date_obj):
                    eventCounter+=1

                    # creating temporary Date Object from event object to use for comparison
                    tempDateObj = event.startDateTime

                    # creating upper bound for comparison
                    tempDateObjMaxBound = tempDateObj.time().replace(minute=tempDateObj.time().minute + 59)

                    # creating lower bound for comparison
                    tempDateObjMinBound = tempDateObj.time().replace(hour=tempDateObj.time().hour - 1, minute=date_obj.time().minute + 1)

                    # comparing both bounds with the user's input event date
                    if date_obj.time() > tempDateObjMaxBound or date_obj.time() < tempDateObjMinBound:
                        print(f'No conflict found for event {eventCounter}')
                    else: #if conflict found, mark canAdd boolean as false
                        canAdd = False
                        print(f'Conflict Found with {tempDateObj}')

                #simple comparison of boolean canAdd
                if(canAdd):
                    event = Appointment(name, tNumber, date_obj, appointmentType)
                    self.listOfEvents.append(event)
                    print("\nEvent added")
                else:
                    print("\nEvent cannot be added. Timing already booked")
            #add event if no same dates are found
            else:
                event = Appointment(name, tNumber, date_obj, appointmentType)
                self.listOfEvents.append(event)
                print("\nEvent added")
        else:
            print('Wrong Input')

    #method to get evets on the same date
    def getEventForDate(self, date):

        tempEventsList = []
        for event in self.listOfEvents:
            if event.getDate() == date.date():
                tempEventsList.append(event)
        return tempEventsList
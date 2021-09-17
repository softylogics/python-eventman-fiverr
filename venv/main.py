from AppointmentBook import AppointmentBook
from datetime import datetime




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    appointmentBook = AppointmentBook()
    #while loop to let the program run continuously
    while 1:

        #main menu and user input selction
        print("\n1: Add Event\n2: Find Event by Date")
        userInput = input("\nPlease select an option: ")
        
        if userInput == '1':
            appointmentBook.addEvent() #if user selects 1, call addEvent method
        elif userInput == '2':
            # if user selects 1, show user events in a specific date
            #irst take input of the date
            date = input("Please enter date to find the event (dd-mm-yyyy hh:mm): ")
            date = date + ' 00:00' #add a mock time to complete the datetime object
            try:
                date_obj = datetime.strptime(date, '%d-%m-%Y %H:%M')  # create datetime object
            except ValueError:
                print('Please input correct date/time format')
                exit()
            except:
                print("An exception occurredd")
                exit()
            listEvents = appointmentBook.getEventForDate(date_obj) #call method to get events and save in a list
            eventCounter = 1
            
            #show events in order
            for event in listEvents:
                print(f"\nEvent {eventCounter}")
                print(event.toString())
                eventCounter += 1
        else:
            print('Wrong input')



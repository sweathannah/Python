import csv #to handle csv file operations
from datetime import datetime

reservations_file = 'reservations.csv' #Define the name of the csv file where reservations will be stored

tables = [
    {'Table1':"Couple's Delight", 'Seats': 2},
    {'Table2':'Cozy Cornert', 'Seats': 2},
    {'Table3':'Intimate Alcove', 'Seats': 2},
    {'Table4':'Family Feast', 'Seats': 4},
    {'Table5':"Friends' Reunion", 'Seats': 4},
    {'Table6':'Royal Banquet', 'Seats': 6},
    {'Table7':'Elite Lounge', 'Seats': 6},
    {'Table8':'Prestige Parlor', 'Seats': 8},
    {'Table9':'Executive Suite', 'Seats': 8 },
    {'Table10':'Grand Gala', 'Seats': 9},
]

def view_tables(tables):
    for i in tables:
        table_name = list(i.keys())[0]
        table_description = i[table_name]
        seats = i['Seats']
        print(f" {table_description} - {seats} seats")

def validate_phone(contact):
    while len(contact) > 11 or len(contact) < 10:
        print("Invalid phone number")
        contact = input("Enter your new contact (if no new contact re-enter the previous contact): ")
    return contact

def validate_date(date):
    while True:
        try:
            date_input = datetime.strptime(date, '%Y-%m-%d')
            if date_input < datetime.now():
                print("The date cannot be in the past. Please enter a valid future date.")
                date = input("Enter the new date for the event (if no new date re-enter the previous date): ")
            else:
                return date
        except ValueError:
            print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")
            date = input("Enter the new date for the event (if no new date re-enter the previous date): ")

def validate_time(time):
    while True:
        try:
            datetime.strptime(time, "%H:%M")
            return time
        except:
            print("Invalid time. Please enter a valid time in the format HH:MM.")
            time = input("Enter your new start time (if no new start-time re-enter the previous start-time): ")


def make_reservation(tables, reservations_file):
    """
    Makes a reservation for a table at a restaurant.

    This function interacts with the user to collect necessary details for making a reservation. 
    It performs the following tasks:
    1. Prompts the user for their name and contact number, ensuring the phone number is valid.
    2. Asks for the number of guests and determines which tables are available based on the party size.
       - If no tables are available for the given party size, the user is prompted to enter a new party size.
    3. Displays the available tables and prompts the user to select a desired table by name.
       - Validates that the selected table name is from the list of available tables.
    4. Asks for the date of the event and ensures the date is in the correct format and in the future.
    5. Prompts the user for the event start time and end time, ensuring both times are valid.
    6. Compiles all the reservation details into a new row and appends this information to the reservations CSV file.
       - If any error occurs during the saving process, an appropriate error message is displayed.

    """
    name = str(input("Enter your name: ")).lower().strip()

    contact = validate_phone((input("Enter your contact number: +234 "))).strip()
    
    party_size = int(input("Enter the number of guests for the event: "))
    available_tables = [table for table in tables if table['Seats'] >= party_size]

    while not available_tables:
        print("No available tables for your party size.")
        party_size = int(input("Enter the number of guests for the event: "))
        available_tables = [table for table in tables if table['Seats'] >= party_size]

    view_tables(available_tables)

    table_names = [list(table.values())[0] for table in available_tables]  # List of table descriptions available for reservation

    table_name = input("Enter the desired table name: ")
    while table_name not in table_names:
        print("Invalid table name. Please choose a valid table from the list.")
        view_tables(available_tables)
        table_name = input("Enter the desired table name: ")

    date = validate_date(input("Enter date of event (YYY-MM-DD): "))
    
    start_time = validate_time(input("Enter event start-time (HH:MM): "))

    end_time = validate_time(input("Enter event end-time (HH:MM): ")
    )

    #Create a list to store each reservation details.
    new_row = [table_name, name, contact, party_size, date, start_time, end_time]

    #Open the reservation file in an append mode.
    try:
        with open(reservations_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        print(f"{table_name} reserved successfully for {name} for the event on {date} from {start_time} to {end_time}.")
    except Exception as error:
        print(f"Error saving reservation: {error}")

def cancel_reservation(reservations_file):
    
    """
    Cancels a reservation by removing it from the reservations CSV file.

    This function interacts with the user to collect the necessary details to identify and cancel an existing reservation. 
    It performs the following tasks:
    1. Prompts the user for their name and the table name they reserved.
    2. Reads the current reservations from the CSV file.
    3. Searches for a matching reservation and removes it if found.
    4. Writes the updated reservations back to the CSV file.
    5. Notifies the user whether the cancellation was successful or if the reservation was not found.

    """
    name_to_cancel = str(input("Enter the name you input while making reservation: ")).strip().lower()
    table_name_to_cancel = str(input("Enter the table name you've resevered: "))

    with open(reservations_file, mode='r') as file:
        reader = csv.reader(file)
        opened_reservation_file = list(reader) #Save the reader object to a     variable and change to list to allow modification since by default, it is now an iterator and can't be modified.

    for reserved_table in opened_reservation_file:
        if reserved_table[1] == name_to_cancel and reserved_table[0] == table_name_to_cancel: 
            del opened_reservation_file[opened_reservation_file.index(reserved_table)] #Identify the reservation with the index from the file content and delete.
        print(f"Reservation for {name_to_cancel} who booked {table_name_to_cancel} has been successfully cancelled!")
        break
    else :
        print("Name not found.")

    with open(reservations_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(opened_reservation_file)

def view_reservations(reservations_file):
    
    """
    Displays all reservations from the reservations CSV file.

    This function reads and displays all reservations stored in the CSV file. 
    It performs the following tasks:
    1. Reads the reservations from the CSV file.
    2. Prints the reservation details in a readable format.

    """
     
    try:
        with open(reservations_file, mode='r') as file:
            reader = csv.reader(file)
            for i in reader:
                print(i)
    except Exception as e:
        print(f"Error viewing reservations: {e}")



def modify_reservation(reservations_file):

    """
    Modifies an existing reservation by updating its details in the reservations CSV file.

    This function interacts with the user to collect the necessary details to identify and modify an existing reservation. 
    It performs the following tasks:
    1. Prompts the user for their name and the table name they reserved.
    2. Reads the current reservations from the CSV file.
    3. Searches for a matching reservation and updates its details if found.
    4. Writes the updated reservations back to the CSV file.
    5. Notifies the user whether the modification was successful or if the reservation was not found.
    """

    name_to_modify = input("Enter the name you used while making the reservation: ").strip().lower()
    table_name_to_modify = input("Enter the table name you've reserved: ")

    with open(reservations_file, mode='r') as file:
        reader = csv.reader(file)
        opened_reservation_file = list(reader)

    for reserved_table in opened_reservation_file:
        if reserved_table[1] == name_to_modify and reserved_table[0] == table_name_to_modify:
            print(f"Reservation for {name_to_modify} who booked {table_name_to_modify} found: \n {reserved_table}")
            
            new_name = input("Enter the new name for your reservation (if no new name re-enter the previous name): ")
            new_contact = validate_phone(input("Enter your new contact (if no new contact re-enter the previous contact): +234 "))
            
            party_size = int(input("Enter the number of guests for the event: "))
            available_tables = [table for table in tables if table['Seats'] >= party_size]

            while not available_tables:
                print("No available tables for your party size.")
                party_size = int(input("Enter the number of guests for the event: "))
                available_tables = [table for table in tables if table['Seats'] >= party_size]

            view_tables(available_tables)

            table_names = [list(table.values())[0] for table in available_tables]  # List of table descriptions available for reservation

            table_name = input("Enter the desired table name: ")
            while table_name not in table_names:
                print("Invalid table name. Please choose a valid table from the list.")
                view_tables(available_tables)
                table_name = input("Enter the desired table name: ")

            new_date = validate_date(input("Enter the new date for the event (if no new date re-enter the previous date): "))
            new_start_time = validate_time(input("Enter your new start time (if no new start-time re-enter the previous start-time): "))
            new_end_time = validate_time(input("Enter your new end time (if no new end-time re-enter the previous end-time): "))

            reserved_table[:] = [table_name, new_name, new_contact, party_size, new_date, new_start_time, new_end_time]

            with open(reservations_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(opened_reservation_file)
            print(f"Reservation for {name_to_modify} at {table_name_to_modify} has been successfully modified.\n {reserved_table[:]}")
            break
    else:
        print(f"Reservation for {name_to_modify} who booked {table_name_to_modify} not found")

def daily_summary(reservations_file):

    """
    Provides a summary of reservations for a specific date.

    This function reads the reservations from the CSV file and displays a summary of reservations for the specified date. 
    It performs the following tasks:
    1. Reads the reservations from the CSV file.
    2. Filters the reservations for the specified date.
    3. Prints the summary of reservations for that date.

    """
    summary_type = input("Do you want to view today's summary or enter a specific date? (Enter 'today' or 'date'): ").strip().lower()
    if summary_type == "today":
        summary_date = datetime.now().strftime('%Y-%m-%d')
    elif summary_type == "date":
        summary_date = validate_date(input("Enter the date for summary (YYYY-MM-DD): "))
    else:
        print("Invalid choice. Please enter 'today' or 'date'.")
        return

    try:
        with open(reservations_file, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            if headers:
                print(", ".join(headers))
                print("-" * 72)
            for reservation in reader:
                if reservation[4] == summary_date:
                    print(", ".join(reservation))
    except Exception as e:
        print(f"Error generating daily summary: {e}")

def menu():
    while True:
        print("\nWelcome! How can we help you?")
        print("1. Make a reservation")
        print("2. Cancel a reservation")
        print("3. Modify a reservation")
        print("4. View reservations")
        print("5. View daily summary")
        print("6. Exit")
        choice = int(input("Choose a request (1-5): "))
         
        if choice == 1:
            make_reservation(tables, reservations_file)
        elif choice == 2:
            cancel_reservation(reservations_file)
        elif choice == 3:
            modify_reservation(reservations_file)
        elif choice == 4:
            view_reservations(reservations_file)
        elif choice == 5:
            daily_summary(reservations_file)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

menu()


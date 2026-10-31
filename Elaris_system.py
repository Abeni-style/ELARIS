# ================= ELARIS SYSTEM =================
users = {"admin": "1234"}
destinations = ["Addis Ababa to Dubai", "Addis Ababa to Nairobi", "Addis Ababa to London"]
seats = []
ticket = {}
economy_price = 10000
business_price = 25000
first_price = 40000
#  INTRODUCTION 
print("""==============================================================================================================================\n           INTRODUCTION TO ELARIS FLIGHT SYSTEM\n==============================================================================================================================\n
ELARIS (Ethiopian Local Airline Reservation & Information System) is ad_choose Python-based airline booking simulation system that helps users reserve flights in an organized and simple way.\nThe system begins with ad_choose welcome page where the user can either register ad_choose new account or log in using existing credentials.\nAfter successful login, the user enters the main menu, where they can:\n# search available flights\n# book tickets\n# view bookings\n# cancel reservations.\nDuring the booking process:\n√the user selects ad_choose destination and flight,\n√chooses ad_choose travel  class_choose such as Economy, Business, or First Classand enters passenger information including name phone number and ID details.\nThe system then displays available seats and prevents already booked seats from being selected again.\nOnce the user confirms the booking,ELARIS automatically generates ad_choose digital ticket containing the passenger details, seat number, flight information,  class_choose type and ticket ID.All booking information is stored using Python file handling so the data remains saved even after the program closes.\nThe system is designed to simulate the basic workflow of ad_choose realairline reservation system while using beginner-level Python concepts such as:loops, conditions, lists, dictionaries, and file handling.\n=============================================================================================================================""")
#  MAIN MENU 
while True:
    print("\n================ MAIN MENU ================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")                
    print("==========================================")
    choice = input("Choose: ")
#  REGISTER 
    if choice == "1":
        print("\n================ REGISTER ================")
        user_name = input("Username: ")
        for char in user_name:
            if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                user_name=""
            if user_name =="":
                print("invalid username. Letters only!")
        pin = input("Password: ")
        users[user_name] = pin
        print("\nRegistered successfully\n")
#  LOGIN 
    elif choice == "2":
        print("\n================ LOGIN ================")
        user_name = input("Username: ")
        pin = input("Password: ")
#  ADMIN 
        if user_name == "vibe" and pin == "abc":
            while True:
                print("""
================ ADMIN DASHBOARD ================
1. View Statistics
2. Change Prices
3. Add Destination
4. View Users
5. Exit Admin Mode
=================================================
""")
                ad_choose = input("Choose: ")
                if ad_choose == "1":
                    print("\n================ STATISTICS ================")
                    print("Tickets Sold:", len(seats), "\n")
                elif ad_choose == "2":
                    print("\n================ PRICES ================")
                    print("1. Economy Class   -", economy_price)
                    print("2. Business Class  -", business_price)
                    print("3. First Class     -", first_price, "\n")
                    change_price = input("Choose: ")
                    if change_price == "1":
                        economy_price = int(input("New Economy Price: "))
                    elif change_price == "2":
                        business_price = int(input("New Business Price: "))
                    elif change_price == "3":
                        first_price = int(input("New First Class Price: "))
                    print("\nUpdated successfully\n")
                elif ad_choose == "3":
                    print("\n================ ADD DESTINATION ================")
                    new_dest = input("New destination: ")
                    destinations.append("Addis Ababa to " + new_dest)
                    print("\nAdded successfully\n")
                elif ad_choose == "4":
                    print("\n================ USERS ================")
                    for i in users:
                        print("-", i)
                    print("")
                elif ad_choose == "5":
                    print("\nExiting admin mode...\n")
                    break
#  USER 
        elif user_name in users and users[user_name] == pin:
            print("\nLogged in Successfully\n")
            while True:
                print("\n================ USER MENU ================")
                print("1. View Flights")
                print("2. Book Ticket")
                print("3. View Ticket")
                print("4. Cancel Booking")
                print("5. Logout")
                print("==========================================")
                menu = input("Choose: ")
# view flights
                if menu == "1":
                    print("\n================ FLIGHTS ================")
                    for i, new_dest in enumerate(destinations, 1):
                        print(i, new_dest)
                    print("")
# book ticket
                elif menu == "2":
                    print("\n================ DESTINATIONS ================")
                    number = 1
                    for new_dest in destinations:
                        print(number, new_dest)
                        number += 1
                    new_dest = input("Choose destination: ")
                    if new_dest == "1":
                        dest = destinations[0]
                    elif new_dest == "2":
                        dest = destinations[1]
                    elif new_dest == "3":
                        dest = destinations[2]
                    elif new_dest == "4":
                        dest = destinations[3]
                    elif new_dest == "5":
                        dest = destinations[4]
                    else:
                        print("\nInvalid destination\n")
                        continue
                    print("\n================ CLASS SELECTION ================")
                    print("1. Economy Class   -", economy_price)
                    print("2. Business Class  -", business_price)
                    print("3. First Class     -", first_price, "\n")
                    class_choose = input("Choose class: ")
                    name = input("Full Name: ")
# -------- PHONE VALIDATION --------
                    phone = input("Phone number (9-12 digits): ")
                    if phone.isdigit():
                        if len(phone) < 9 or len(phone) > 12:
                            print("Invalid phone. Disqualified.")
                            continue
                    else:
                        print("Invalid phone. Disqualified.")
                        continue
# -------- ID VALIDATION --------
                    id_num = input("ID (5-12 characters): ")
                    if len(id_num) < 5 or len(id_num) > 12:
                        print("Invalid ID. Disqualified.")
                        continue
                    seat = int(input("Seat (1-6): "))
                    if seat < 1 or seat > 6:
                        print("\nInvalid seat number\n")
                        continue
                    if seat in seats:
                            print("\nSeat already taken\n")
                            continue
                    seats.append(seat)
                    if  class_choose == "1":
                        cls = "Economy Class"
                        price = economy_price
                    elif  class_choose == "2":
                        cls = "Business Class"
                        price = business_price
                    elif  class_choose == "3":
                        cls = "First Class"
                        price = first_price
                    else:
                        print("\nInvalid  class_choose\n")
                        continue
                    ticket = {
                        "name": name,
                        "phone": phone,
                        "id": id_num,
                        "destination": dest,
                        "seat": seat,
                        " class_choose": cls,
                        "price": price
                    }
                    print("\n================ TICKET CONFIRMED ================")
                    print("Name        :", name, "\n")
                    print("Phone       :", phone, "\n")
                    print("ID          :", id_num, "\n")
                    print("Destination :", dest, "\n")
                    print("Seat        :", seat, "\n")
                    print("Class       :", cls, "\n")
                    print("Price       :", price, "\n")
# view ticket
                elif menu == "3":
                    print("\n================ TICKET ================")
                    if ticket:
                        for key in ticket:
                            print(key, ":", ticket[key])
                    else:
                        print("No ticket found")
# cancel booking
                elif menu == "4":
                    print("\n================ CANCEL ================")
                    seat = int(input("Seat number: "))
                    if seat in seats:
                        seats.remove(seat)
                        ticket = {}
                        print("\nCancelled successfully\n")
                    else:
                        print("\nSeat not found\n")
# logout
                elif menu == "5":
                    print("\nLogging out...\n")
                    break
        else:
            print("\nWrong username or password\n")
#  EXIT 
    elif choice == "3":
        print("\nSystem closed\n")
        break
    else:
        print("\nInvalid menu\n")
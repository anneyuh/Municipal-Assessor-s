requests = []
request_number = 1
resident_accounts = [] 

documents = ["Certified True Copy of Tax Declaration","Certification of Property Ownership","Tax Clearance"]

requirements = [["Valid ID", "Request Form"],["Valid ID", "Request Form"],["Valid ID", "Request Form"]]

statuses = ["Submitted","Under Review","Action Required","Ready for Processing","Ready for Release","Released"]

appointment_statuses = ["Booked","Completed","Cancelled","Missed"]

appointments = []

slots = [["October 19, 2026", "9:00 AM - 9:30 AM", 5, 0],["October 19, 2026", "9:30 AM - 10:00 AM", 5, 0],["October 20, 2026", "9:00 AM - 9:30 AM", 5, 0]]

def show_available_documents():
    print()
    print("  ✦ AVAILABLE DOCUMENTS ✦")
    print("------------------------------")

    i = 0  
    for document in documents:
        print()
        print("➜ ", document)  
        print("Requirements:")
        for requirement in requirements[i]:
            print("   •", requirement)
        i = i + 1
    print("------------------------------") 

def check_request_status(username):
    print()
    print("       ✦ REQUEST TRACKING ✦")
    print("------------------------------")

    reference_no = input("Enter reference number (or B to go back): ")

    if reference_no == "B" or reference_no == "b":
        return

    found = False

    for request in requests:
        if request[0] == reference_no:
            if request[1] == username:
                print()
                print("Request Found")
                print("Reference Number:", request[0])
                print("Requester Name:", request[2])
                print("Property Owner:", request[3])
                print("Document Requested:", request[4])
                print("Tax Declaration Number:", request[5])
                print("Property Location:", request[6])
                print("Purpose:", request[7])
                print("Status:", request[8])

                if request[8] == "Submitted":
                    print("Next Step: Your request is waiting for staff review.")

                elif request[8] == "Under Review":
                    print("Next Step: Staff are reviewing your request.")

                elif request[8] == "Action Required":
                    print("Next Step: Please address the missing requirements.")

                elif request[8] == "Ready for Processing":
                    print("Next Step: Your requirements have been verified.")

                elif request[8] == "Ready for Release":
                    print("Next Step: Your document is ready for release.")

                elif request[8] == "Released":
                    print("Next Step: Your document has been released.")

                if request[9] == "":
                    print("No staff instructions recorded.")
                else:
                    print("Staff Instructions:", request[9])

                print("------------------------------")
                found = True
                break

    if found == False:
        print()
        print("Request not found in your account.")
        print("Please check your reference number.")
        print("------------------------------")
 
def book_appointment(username):
    print()
    print("      ✦ BOOK APPOINTMENT ✦")
    print("------------------------------")

    reference_no = input("Enter request reference number (or B to go back): ")

    if reference_no == "B" or reference_no == "b":
        return

    found = False

    for request in requests:
        if request[0] == reference_no and request[1] == username:
            found = True

            if request[8] == "Submitted" or request[8] == "Action Required":
                print()
                print("Request Found:", request[0])
                print("➜", request[4])
                print("Appointment is available for requirements verification.")
            else:
                print()
                print("Your request is not eligible for an appointment.")
                print("------------------------------")
                return

    if found == False:
        print()
        print("Request not found in your account.")
        print("------------------------------")
        return

    for appointment in appointments:
        if appointment[0] == reference_no:
            if appointment[4] == "Booked":
                print()
                print("This request already has a booked appointment.")
                print("Please check your appointment details.")
                print("------------------------------")
                return

    print()
    print("AVAILABLE APPOINTMENT SLOTS")
    print("------------------------------")

    i = 0

    for slot in slots:
        if slot[3] < slot[2]:
            print(i + 1, "-", slot[0])
            print("     Time:", slot[1])
            print("     Available places:", slot[2] - slot[3])
        else:
            print(i + 1, "-", slot[0])
            print("     Time:", slot[1])
            print("     FULL")

        i = i + 1

    print("------------------------------")
    print("Enter B to cancel booking.")

    slot_number = input("Choose an appointment slot: ")

    while not (
        slot_number == "1"
        or slot_number == "2"
        or slot_number == "3"
        or slot_number == "B"
        or slot_number == "b"
    ):
        print("Please enter a valid slot number or B to go back.")
        slot_number = input("Choose an appointment slot: ")

    if slot_number == "B" or slot_number == "b":
        return

    selected_slot = slots[int(slot_number) - 1]

    while selected_slot[3] >= selected_slot[2]:
        print()
        print("Sorry, this appointment slot is full.")
        print("Please choose another available slot.")
        print()
        print("AVAILABLE APPOINTMENT SLOTS")
        print("------------------------------")

        i = 0

        for slot in slots:
            if slot[3] < slot[2]:
                print(i + 1, "-", slot[0])
                print("     Time:", slot[1])
                print("     Available places:", slot[2] - slot[3])
            else:
                print(i + 1, "-", slot[0])
                print("     Time:", slot[1])
                print("     FULL")

            i = i + 1

        print("------------------------------")
        print("Enter B to cancel booking.")

        slot_number = input("Choose another appointment slot: ")

        while not (
            slot_number == "1"
            or slot_number == "2"
            or slot_number == "3"
            or slot_number == "B"
            or slot_number == "b"
        ):
            print("Please enter a valid slot number or B to go back.")
            slot_number = input("Choose another appointment slot: ")

        if slot_number == "B" or slot_number == "b":
            return

        selected_slot = slots[int(slot_number) - 1]

    appointment = [
        reference_no,
        username,
        selected_slot[0],
        selected_slot[1],
        "Booked"
    ]

    appointments.append(appointment)
    selected_slot[3] = selected_slot[3] + 1

    print()
    print("Appointment booked successfully!")
    print("Request Reference:", reference_no)
    print("Date:", selected_slot[0])
    print("Time:", selected_slot[1])
    print("Appointment Status: Booked")
    print("------------------------------")

def my_appointments(username):
    print()
    print("      ✦ MY APPOINTMENTS ✦")
    print("------------------------------")

    found = False

    for appointment in appointments:
        if appointment[1] == username:
            print()
            print("Request Reference:", appointment[0])

            for request in requests:
                if request[0] == appointment[0]:
                    print("➜", request[4])

            print("Date:", appointment[2])
            print("Time:", appointment[3])
            print("Appointment Status:", appointment[4])
            print("------------------------------")

            found = True

    if found == False:
        print("You have no appointments yet.")
        print("------------------------------")

def cancel_appointment(username):
    print()
    print("     ✦ CANCEL APPOINTMENT ✦")
    print("------------------------------")

    found = False

    for appointment in appointments:
        if appointment[1] == username:
            if appointment[4] == "Booked":
                found = True

                for request in requests:
                    if request[0] == appointment[0]:
                        print()
                        print("Reference Number:", appointment[0])
                        print("Document:", request[4])
                        print("Date:", appointment[2])
                        print("Time:", appointment[3])
                        print("Status:", appointment[4])

    if found == False:
        print()
        print("No booked appointments found.")
        print("------------------------------")
        return

    print()
    reference_no = input("Enter the reference number to cancel: ")

    appointment_found = False

    for appointment in appointments:
        if appointment[0] == reference_no:
            if appointment[1] == username:
                if appointment[4] == "Booked":
                    appointment_found = True

                    print()
                    print("[1] - Confirm Cancellation")
                    print("[2] - Keep Appointment")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        appointment[4] = "Cancelled"

                        for slot in slots:
                            if slot[0] == appointment[2]:
                                if slot[1] == appointment[3]:
                                    slot[3] = slot[3] - 1

                        print("Appointment cancelled successfully.")

                    elif choice == "2":
                        print("Appointment remains booked.")

                    else:
                        print("Invalid choice. No changes were made.")

                    break

    if appointment_found == False:
        print()
        print("No booked appointment found for that reference number.")

    print("------------------------------")

def my_requests_and_appointments(username):
    while True:
        print()
        print("  ✦ MY REQUESTS AND APPOINTMENTS ✦")
        print("------------------------------")
        print("[1] - View My Requests")
        print("[2] - Track Request Status")
        print("[3] - View My Appointments")
        print("[4] - Back")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            my_requests(username)

        elif choice == "2":
            check_request_status(username)

        elif choice == "3":
            my_appointments(username)

        elif choice == "4":
            return

        else:
            print("Please enter a valid choice.")

def record_request(request_number, username):
    print()
    print("  ✦ SUBMIT DOCUMENT REQUEST ✦")
    print("------------------------------")

    name = ""

    for account in resident_accounts:
        if account[0] == username:
            name = account[2]

    if name == "":
        print("Unable to retrieve your account name.")
        return request_number

    print("Requester Name:", name)

    print()
    print("Available Documents:")
    print("------------------------------")

    i = 0

    for document in documents:
        print(i + 1, "-", document)
        i = i + 1

    print()
    document_number = input("Enter document number (or B to go back): ")

    while not (
        document_number == "1"
        or document_number == "2"
        or document_number == "3"
        or document_number == "B"
        or document_number == "b"
    ):
        print("Please enter a valid document number.")
        document_number = input("Enter document number (or B to go back): ")

    if document_number == "B" or document_number == "b":
        return request_number

    document = documents[int(document_number) - 1]
    document_index = int(document_number) - 1

    print()
    owner_name = input("Enter property owner's full name: ")

    while owner_name == "":
        print("Please enter the property owner's full name.")
        owner_name = input("Enter property owner's full name: ")

    print()
    tax_number = input("Enter Tax Declaration Number (or press Enter if unknown): ")

    print()
    property_location = input("Enter property location or barangay: ")

    while property_location == "":
        print("Please enter the property location or barangay.")
        property_location = input("Enter property location or barangay: ")

    print()
    purpose = input("Why do you need this document? ")

    while purpose == "":
        print("Please enter the purpose of your request.")
        purpose = input("Why do you need this document? ")

    reference_no = "MAO-" + str(request_number).zfill(3)

    request = [
        reference_no,
        username,
        name,
        owner_name,
        document,
        tax_number,
        property_location,
        purpose,
        "Submitted",
        ""
    ]

    requests.append(request)

    print()
    print("Your document request has been submitted.")
    print("Reference Number:", reference_no)
    print("Document Requested:", document)
    print("Current Status: Submitted")
    print("Please save your reference number for tracking.")
    print("------------------------------")

    print()
    print("➜ ", document)
    print("Requirements:")

    for requirement in requirements[document_index]:
        print("   •", requirement)

    print("------------------------------")

    print("[1] - Book an Appointment")
    print("[2] - Book Later")
    print("------------------------------")

    choice = input("Enter your choice: ")

    while not (choice == "1" or choice == "2"):
        print("Please enter 1 or 2.")
        choice = input("Enter your choice: ")

    if choice == "1":
        book_appointment(username)

    else:
        print("You can book your appointment later from the dashboard.")

    return request_number + 1

def request_monitoring():
    while True:
        print()
        print("     ✦ REQUEST MONITORING ✦")
        print("------------------------------")

        counts = [0, 0, 0, 0, 0, 0]

        for request in requests:
            i = 0

            for status in statuses:
                if request[8] == status:
                    counts[i] = counts[i] + 1

                i = i + 1

        total = 0

        for count in counts:
            total = total + count

        print("Total Requests:", total)

        i = 0

        for status in statuses:
            print(status + ":", counts[i])
            i = i + 1

        print("------------------------------")
        print("[1] - View All Requests")
        print("[2] - Find Request")
        print("[3] - View Requests by Status")
        print("[4] - Back")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            if requests == []:
                print("No document requests have been recorded.")
            else:
                print()
                print("ALL DOCUMENT REQUESTS")
                print("------------------------------")

                for request in requests:
                    print("Reference Number:", request[0])
                    print("Requester:", request[2])
                    print("Property Owner:", request[3])
                    print("Document:", request[4])
                    print("Tax Declaration Number:", request[5])
                    print("Property Location:", request[6])
                    print("Purpose:", request[7])
                    print("Status:", request[8])
                    print("Staff Instructions:", request[9])
                    print("------------------------------")

        elif choice == "2":
            reference_no = input("Enter reference number: ")

            found = False

            for request in requests:
                if request[0] == reference_no:
                    print()
                    print("Reference Number:", request[0])
                    print("Requester:", request[2])
                    print("Property Owner:", request[3])
                    print("Document:", request[4])
                    print("Tax Declaration Number:", request[5])
                    print("Property Location:", request[6])
                    print("Purpose:", request[7])
                    print("Status:", request[8])
                    print("Staff Instructions:", request[9])
                    print("------------------------------")

                    found = True
                    break

            if found == False:
                print("Request not found.")

        elif choice == "3":
            print()
            print("Available Statuses:")

            i = 0

            for status in statuses:
                print(i + 1, "-", status)
                i = i + 1

            status_number = input("Enter status number: ")

            while not (
                status_number == "1"
                or status_number == "2"
                or status_number == "3"
                or status_number == "4"
                or status_number == "5"
                or status_number == "6"
            ):
                print("Please enter a valid status number.")
                status_number = input("Enter status number: ")

            selected_status = statuses[int(status_number) - 1]

            print()
            print("Requests with status:", selected_status)
            print("------------------------------")

            found = False

            for request in requests:
                if request[8] == selected_status:
                    print("Reference Number:", request[0])
                    print("Requester:", request[2])
                    print("Document:", request[4])
                    print("Property Location:", request[6])
                    print("Status:", request[8])
                    print("------------------------------")

                    found = True

            if found == False:
                print("No requests found with this status.")

        elif choice == "4":
            return

        else:
            print("Please enter a valid choice.")
    
def update_status():
    print()
    print("     ✦ UPDATE REQUEST STATUS ✦")
    print("------------------------------")

    reference_no = input("Enter reference number (or B to go back): ")

    if reference_no == "B" or reference_no == "b":
        return

    found = False

    for request in requests:
        if request[0] == reference_no:
            found = True

            print()
            print("Reference Number:", request[0])
            print("Requester:", request[2])
            print("Property Owner:", request[3])
            print("Document:", request[4])
            print("Current Status:", request[8])

            if request[8] == "Submitted":
                print()
                print("[1] - Change to Under Review")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Under Review"
                    print("Request status updated successfully.")
                    print("New Status:", request[8])

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

                else:
                    print("Invalid choice. No changes were made.")

            elif request[8] == "Under Review":
                print()
                print("Use Verify Requirements to record")
                print("whether the requirements are complete.")
                print()
                print("[1] - Go to Status Menu")
                print("[2] - Cancel")

                choice = input("Enter your choice: ")

                if choice == "1":
                    print("Please use Verify Requirements")
                    print("to update this request.")
                elif choice == "2":
                    print("Status update cancelled.")
                else:
                    print("Invalid choice.")

            elif request[8] == "Action Required":
                print()
                print("The resident must address the instructions.")
                print("[1] - Resume Review")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                if choice == "1":
                    print("Please use Resume Request Review")
                    print("to record the resident's response.")

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

                else:
                    print("Invalid choice. No changes were made.")

            elif request[8] == "Ready for Processing":
                print()
                print("[1] - Change to Ready for Release")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Ready for Release"
                    print("Request status updated successfully.")
                    print("New Status:", request[8])

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

                else:
                    print("Invalid choice. No changes were made.")

            elif request[8] == "Ready for Release":
                print()
                print("[1] - Confirm Document Released")
                print("[2] - Keep Current Status")
                print("[3] - Cancel")

                choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Released"
                    print("Request status updated successfully.")
                    print("New Status:", request[8])

                elif choice == "2":
                    print("The current status remains unchanged.")

                elif choice == "3":
                    print("Status update cancelled.")

                else:
                    print("Invalid choice. No changes were made.")

            elif request[8] == "Released":
                print()
                print("This document has already been released.")
                print("No further status changes are available.")

            break

    if found == False:
        print()
        print("Request not found.")

    print("------------------------------")

def verify_requirements():
    print()
    print("     ✦ VERIFY REQUIREMENTS ✦")
    print("------------------------------")

    reference_no = input("Enter the resident's request reference number: ")

    found = False

    for request in requests:
        if request[0] == reference_no:
            found = True

            print()
            print("Reference Number:", request[0])
            print("Requester:", request[2])
            print("Property Owner:", request[3])
            print("Document:", request[4])
            print("Current Status:", request[8])

            if request[8] == "Released":
                print("This request has already been released.")
                return

            if request[8] == "Ready for Release":
                print("This request is already ready for release.")
                return

            print()
            print("[1] - Requirements Complete")
            print("[2] - Requirements Incomplete")
            print("[3] - Cancel")
            print("------------------------------")

            choice = input("Enter your choice: ")

            if choice == "1":
                request[8] = "Ready for Processing"
                request[9] = "Requirements verified as complete."

                for appointment in appointments:
                    if appointment[0] == reference_no:
                        if appointment[4] == "Booked":
                            appointment[4] = "Completed"

                print("Requirements marked as complete.")
                print("New Status:", request[8])
                print("Appointment Status: Completed")

            elif choice == "2":
                notes = input("Enter missing requirements or instructions: ")

                while notes == "":
                    print("Please provide the missing requirements.")
                    notes = input("Enter missing requirements or instructions: ")

                request[8] = "Action Required"
                request[9] = notes

                for appointment in appointments:
                    if appointment[0] == reference_no:
                        if appointment[4] == "Booked":
                            appointment[4] = "Completed"

                print("Request marked for further action.")
                print("Instructions:", request[9])
                print("Appointment Status: Completed")

            elif choice == "3":
                print("Verification cancelled.")

            else:
                print("Invalid choice. No changes were made.")

            break

    if found == False:
        print()
        print("Request not found.")

    print("------------------------------")

def resume_review():
    print()
    print("       ✦ RESUME REQUEST REVIEW ✦")
    print("------------------------------")

    reference_no = input("Enter request reference number: ")

    found = False

    for request in requests:
        if request[0] == reference_no:
            found = True

            print()
            print("Reference Number:", request[0])
            print("Requester:", request[2])
            print("Property Owner:", request[3])
            print("Document:", request[4])
            print("Current Status:", request[8])

            if request[8] == "Action Required":
                print()
                print("Confirm that the resident has addressed")
                print("the recorded requirements.")

                print("[1] - Resident has responded")
                print("[2] - Not yet resolved")

                choice = input("Enter your choice: ")

                if choice == "1":
                    request[8] = "Under Review"
                    request[9] = "Resident response received. Requirements need rechecking."

                    print("Request returned to Under Review.")

                elif choice == "2":
                    print("Request remains Action Required.")

                else:
                    print("Invalid choice. No changes were made.")

            else:
                print("Only requests marked Action Required")
                print("can be returned to review.")

            break

    if found == False:
        print("Request not found.")

    print("------------------------------")

def staff_login():
    print()
    print("      ✦ STAFF LOGIN ✦")
    print("------------------------------")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "123":
        print()
        print("Login successful.")
        return True
    else:
        print()
        print("Invalid username or password.")
        return False

def create_account():
    print()
    print("     ✦ CREATE ACCOUNT ✦")
    print("------------------------------")

    name = input("Enter your full name (or B to go back): ")

    if name == "B" or name == "b":
        return

    while name == "":
        print("Please enter your full name.")
        name = input("Enter your full name (or B to go back): ")

        if name == "B" or name == "b":
            return

    username = input("Create a username (or B to go back): ")

    if username == "B" or username == "b":
        return

    while username == "":
        print("Please enter a username.")
        username = input("Create a username (or B to go back): ")

        if username == "B" or username == "b":
            return

    for account in resident_accounts:
        if account[0] == username:
            print("That username is already taken.")
            return

    password = input("Create a password: ")

    while password == "":
        print("Please enter a password.")
        password = input("Create a password: ")

    account = [username, password, name]
    resident_accounts.append(account)

    print()
    print("Your account has been created successfully.")
    print("You can now log in using your username and password.")
    print("------------------------------")

def resident_login():
    print()
    print("       ✦ RESIDENT LOGIN ✦")
    print("------------------------------")

    username = input("Username (or B to go back): ")

    if username == "B" or username == "b":
        return ""

    password = input("Password: ")

    for account in resident_accounts:
        if account[0] == username:
            if account[1] == password:
                print()
                print("Login successful.")
                print("Welcome,", account[2])
                return username

def my_requests(username):
    print()
    print("        ✦ MY REQUESTS ✦")
    print("------------------------------")

    found = False

    for request in requests:
        if request[1] == username:
            print()
            print("Reference Number:", request[0])
            print("Requester Name:", request[2])
            print("Property Owner:", request[3])
            print("➜", request[4])
            print("Tax Declaration Number:", request[5])
            print("Property Location:", request[6])
            print("Purpose:", request[7])
            print("Status:", request[8])
            print("------------------------------")

            found = True

    if found == False:
        print("You have no document requests yet.")
        print("------------------------------")

def resident_dashboard(username, request_number):
    while True:
        print()
        print("     ✦ RESIDENT DASHBOARD ✦")
        print("------------------------------")
        print("[1] - Submit Document Request")
        print("[2] - My Requests and Appointments")
        print("[3] - View Available Documents")
        print("[4] - Cancel Appointment")
        print("[5] - Log Out")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            request_number = record_request(request_number, username)

        elif choice == "2":
            my_requests_and_appointments(username)

        elif choice == "3":
            show_available_documents()

        elif choice == "4":
            cancel_appointment(username)

        elif choice == "5":
            print("You have logged out.")
            return request_number

        else:
            print("Please enter a valid choice.")

def resident_menu(request_number):
    while True:
        print()
        print("     ✦ RESIDENT PORTAL ✦")
        print("------------------------------")
        print("[1] - Log In")
        print("[2] - Create Account")
        print("[3] - Back")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = resident_login()

            if username == "":
                print("Login failed. Please try again.")
            else:
                request_number = resident_dashboard(username, request_number)

        elif choice == "2":
            create_account()

        elif choice == "3":
            return request_number

        else:
            print("Please enter a valid choice.")

def staff_menu(request_number):
    while True:
        print()
        print("        ✦ STAFF MENU ✦")
        print("------------------------------")
        print("[1] - Request Monitoring")
        print("[2] - Verify Requirements")
        print("[3] - Resume Request Review")
        print("[4] - Update Request Status")
        print("[5] - Back")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            request_monitoring()

        elif choice == "2":
            verify_requirements()

        elif choice == "3":
            resume_review()

        elif choice == "4":
            update_status()

        elif choice == "5":
            return request_number

        else:
            print("Please enter a valid choice.")

def main_menu(request_number):
    while True:
        print()
        print("✦ MUNICIPAL ASSESSOR'S OFFICE ✦")
        print("------------------------------")
        print("[1] - Resident")
        print("[2] - Staff")
        print("[3] - Exit")
        print("------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            request_number = resident_menu(request_number)

        elif choice == "2":
            if staff_login():
                request_number = staff_menu(request_number)

        elif choice == "3":
            print()
            print("Thank you for using the system.")
            break

        else:
            print("Please enter a valid choice.")

main_menu(request_number)
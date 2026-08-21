# =========================================================
#               HOTEL MANAGEMENT SYSTEM
#         (with bonus features)
# =========================================================

# ---------------------- ROOM DATA -------------------------
rooms = [101, 102, 103, 104, 105, 201, 202, 203, 301, 302]
room_types = ["Single", "Single", "Double", "Double", "Deluxe",
              "Single", "Double", "Double", "Deluxe", "Deluxe"]
room_prices = [3000, 3000, 5000, 5000, 8000,
               3000, 5000, 5000, 8000, 8000]
room_status = ["Available", "Booked", "Available", "Booked", "Available",
               "Available", "Available", "Available", "Available", "Available"]

# ------------------- CUSTOMER DATA --------------------------
# Each customer is stored as a dictionary inside this list (supports multiple customers).
customers = []

sample_names = ["Ali", "Ahmed"]
sample_rooms = [102, 104]
sample_nights = [2, 3]
sample_phones = ["03001234567", "03111234567"]

for i in range(len(sample_names)):
    room_index = rooms.index(sample_rooms[i])
    customers.append({
        "name": sample_names[i],
        "cnic": "N/A",
        "phone": sample_phones[i],
        "room": sample_rooms[i],
        "room_type": room_types[room_index],
        "nights": sample_nights[i],
        "food_charges": 0,
        "laundry_charges": 0,
        "room_service_charges": 0,
        "discount_percent": 0
    })

# ------------------- HOTEL SETTINGS --------------------------
TAX_RATE = 5            # percent
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
total_revenue = 0        # accumulates every time a customer checks out


# ---------------------- ROOM FUNCTIONS ---------------------------

def show_rooms():
    print("\n========== AVAILABLE ROOMS ==========")
    found = False
    for i in range(len(rooms)):
        if room_status[i] == "Available":
            print(f"Room {rooms[i]} - {room_types[i]} - Rs. {room_prices[i]} - Available")
            found = True
    if not found:
        print("No rooms are currently available.")
    print("======================================")


def find_room_index(room_number):
    if room_number in rooms:
        return rooms.index(room_number)
    return -1


def find_customer_by_room(room_number):
    for customer in customers:
        if customer["room"] == room_number:
            return customer
    return None


# ---------------------- BOOKING ---------------------------

def book_room():
    print("\n========== BOOK A ROOM ==========")
    name = input("Customer Name: ")
    cnic = input("CNIC/ID: ")
    phone = input("Phone Number: ")

    try:
        room_number = int(input("Room Number: "))
    except ValueError:
        print("Invalid room number.")
        return

    index = find_room_index(room_number)

    if index == -1:
        print(f"Room {room_number} does not exist.")
        return

    if room_status[index] != "Available":
        print(f"Room {room_number} is already booked.")
        return

    try:
        nights = int(input("Number of Nights: "))
    except ValueError:
        print("Invalid number of nights.")
        return

    if nights <= 0:
        print("Number of nights must be at least 1.")
        return

    customers.append({
        "name": name,
        "cnic": cnic,
        "phone": phone,
        "room": room_number,
        "room_type": room_types[index],
        "nights": nights,
        "food_charges": 0,
        "laundry_charges": 0,
        "room_service_charges": 0,
        "discount_percent": 0
    })

    room_status[index] = "Booked"

    print("\nBooking Successful!")
    print(f"Customer: {name}")
    print(f"Room: {room_number}")
    print(f"Room Type: {room_types[index]}")
    print(f"Nights: {nights}")


# ---------------------- CUSTOMER INFO ---------------------------

def show_customers():
    print("\n========== CUSTOMER INFORMATION ==========")
    if len(customers) == 0:
        print("No rooms are currently booked.")
        return

    for customer in customers:
        print(f"Customer Name: {customer['name']}")
        print(f"Phone: {customer['phone']}")
        print(f"Room Number: {customer['room']}")
        print(f"Room Type: {customer['room_type']}")
        print(f"Nights: {customer['nights']}")
        print("-" * 30)


# ---------------------- EXTRA SERVICES (BONUS) ---------------------------

def add_extra_charges():
    print("\n===== ADD EXTRA SERVICES =====")
    if len(customers) == 0:
        print("No rooms are currently booked.")
        return

    try:
        room_number = int(input("Enter Room Number: "))
    except ValueError:
        print("Invalid room number.")
        return

    customer = find_customer_by_room(room_number)
    if customer is None:
        print(f"No booking found for Room {room_number}.")
        return

    print("1. Food Order Charges")
    print("2. Laundry Charges")
    print("3. Room Service Charges")
    print("4. Apply Discount (%)")
    choice = input("Select an option (1-4): ")

    if choice == "1":
        amount = float(input("Enter Food Charges (Rs.): "))
        customer["food_charges"] += amount
        print(f"Rs. {amount} added to Food Charges for {customer['name']}.")
    elif choice == "2":
        amount = float(input("Enter Laundry Charges (Rs.): "))
        customer["laundry_charges"] += amount
        print(f"Rs. {amount} added to Laundry Charges for {customer['name']}.")
    elif choice == "3":
        amount = float(input("Enter Room Service Charges (Rs.): "))
        customer["room_service_charges"] += amount
        print(f"Rs. {amount} added to Room Service Charges for {customer['name']}.")
    elif choice == "4":
        percent = float(input("Enter Discount Percentage: "))
        customer["discount_percent"] = percent
        print(f"{percent}% discount applied for {customer['name']}.")
    else:
        print("Invalid choice.")


# ---------------------- BILLING ---------------------------

def compute_bill_details(customer, room_index):
    """Returns a dictionary with the full bill breakdown for a customer."""
    price_per_night = room_prices[room_index]
    nights = customer["nights"]
    room_total = price_per_night * nights

    extras = (customer["food_charges"] +
              customer["laundry_charges"] +
              customer["room_service_charges"])

    subtotal = room_total + extras

    discount_amount = subtotal * (customer["discount_percent"] / 100)
    after_discount = subtotal - discount_amount

    tax_amount = after_discount * (TAX_RATE / 100)
    grand_total = after_discount + tax_amount

    return {
        "price_per_night": price_per_night,
        "nights": nights,
        "room_total": room_total,
        "food_charges": customer["food_charges"],
        "laundry_charges": customer["laundry_charges"],
        "room_service_charges": customer["room_service_charges"],
        "subtotal": subtotal,
        "discount_percent": customer["discount_percent"],
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "grand_total": grand_total
    }


def calculate_bill():
    print("\n========== CALCULATE BILL ==========")
    if len(customers) == 0:
        print("No rooms are currently booked.")
        return

    try:
        room_number = int(input("Enter Room Number: "))
    except ValueError:
        print("Invalid room number.")
        return

    customer = find_customer_by_room(room_number)
    if customer is None:
        print(f"No booking found for Room {room_number}.")
        return

    index = find_room_index(room_number)
    bill = compute_bill_details(customer, index)

    print("\n========== BILL ==========")
    print(f"Customer: {customer['name']}")
    print(f"Room: {room_number}")
    print(f"Price/Night: Rs. {bill['price_per_night']}")
    print(f"Nights: {bill['nights']}")
    print(f"Room Charges: Rs. {bill['room_total']}")
    print(f"Food Charges: Rs. {bill['food_charges']}")
    print(f"Laundry Charges: Rs. {bill['laundry_charges']}")
    print(f"Room Service Charges: Rs. {bill['room_service_charges']}")
    print(f"Subtotal: Rs. {bill['subtotal']}")
    print(f"Discount: {bill['discount_percent']}% (-Rs. {bill['discount_amount']:.2f})")
    print(f"Tax ({TAX_RATE}%): Rs. {bill['tax_amount']:.2f}")
    print(f"Total Bill: Rs. {bill['grand_total']:.2f}")
    print("===========================")


# ---------------------- CHECKOUT ---------------------------

def checkout():
    global total_revenue
    print("\n========== CHECKOUT ==========")
    if len(customers) == 0:
        print("No rooms are currently booked.")
        return

    try:
        room_number = int(input("Enter Room Number: "))
    except ValueError:
        print("Invalid room number.")
        return

    customer = find_customer_by_room(room_number)
    if customer is None:
        print(f"No booking found for Room {room_number}.")
        return

    index = find_room_index(room_number)
    bill = compute_bill_details(customer, index)

    print("\nCheckout Successful!")
    print(f"Customer: {customer['name']}")
    print(f"Room: {room_number}")
    print(f"Total Bill: Rs. {bill['grand_total']:.2f}")

    total_revenue += bill["grand_total"]

    customers.remove(customer)
    room_status[index] = "Available"

    print(f"Room {room_number} is now available.")


# ---------------------- SEARCH (BONUS) ---------------------------

def search_customer_by_name():
    print("\n===== SEARCH CUSTOMER BY NAME =====")
    if len(customers) == 0:
        print("No rooms are currently booked.")
        return

    name = input("Enter customer name: ").strip().lower()
    found = False

    for customer in customers:
        if customer["name"].strip().lower() == name:
            print(f"Customer Name: {customer['name']}")
            print(f"Phone: {customer['phone']}")
            print(f"Room Number: {customer['room']}")
            print(f"Room Type: {customer['room_type']}")
            print(f"Nights: {customer['nights']}")
            print("-" * 30)
            found = True

    if not found:
        print(f"No customer found with the name '{name}'.")


def search_booking_by_room():
    print("\n===== SEARCH BOOKING BY ROOM NUMBER =====")
    if len(customers) == 0:
        print("No rooms are currently booked.")
        return

    try:
        room_number = int(input("Enter Room Number: "))
    except ValueError:
        print("Invalid room number.")
        return

    customer = find_customer_by_room(room_number)
    if customer is None:
        print(f"No booking found for Room {room_number}.")
        return

    print(f"Customer Name: {customer['name']}")
    print(f"Phone: {customer['phone']}")
    print(f"Room Number: {customer['room']}")
    print(f"Room Type: {customer['room_type']}")
    print(f"Nights: {customer['nights']}")


# ---------------------- ADMIN PANEL (BONUS) ---------------------------

def admin_login():
    print("\n===== ADMIN LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


def show_total_revenue():
    if admin_login():
        print("\n========== TOTAL HOTEL REVENUE ==========")
        print(f"Total Revenue (from checked-out customers): Rs. {total_revenue:.2f}")
        print("===========================================")


# ---------------------- MENU ---------------------------

def show_menu():
    print("\n====================================")
    print("       HOTEL MANAGEMENT SYSTEM")
    print("====================================")
    print("1. Show Available Rooms")
    print("2. Book a Room")
    print("3. Customer Information")
    print("4. Add Extra Charges (Food/Laundry/Room Service/Discount)")
    print("5. Calculate Bill")
    print("6. Checkout")
    print("7. Search Customer by Name")
    print("8. Search Booking by Room Number")
    print("9. Admin Panel (Total Revenue)")
    print("10. Exit")
    print("====================================")


# ---------------------- MAIN PROGRAM ---------------------------

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            show_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            show_customers()
        elif choice == "4":
            add_extra_charges()
        elif choice == "5":
            calculate_bill()
        elif choice == "6":
            checkout()
        elif choice == "7":
            search_customer_by_name()
        elif choice == "8":
            search_booking_by_room()
        elif choice == "9":
            show_total_revenue()
        elif choice == "10":
            print("\nThank you for using Hotel Management System!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()

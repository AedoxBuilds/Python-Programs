# ================================================================
#              GROCERY MANAGEMENT SYSTEM  (DEBUGGED)
# ================================================================
# Console Based Inventory, POS, Warehouse & Analytics System
#
# Concepts used:
# Variables
# Lists
# Dictionaries
# for loops
# while loops
# if / elif / else
# input()
# calculations
# string formatting
#
# No custom functions are used.
#
# --- FIXES IN THIS VERSION (see NOTES.md for the full list) ---
# 1. All totals/reports (Dashboard, Profit & Loss, Low Stock Alerts,
#    Sales Analytics, Financial Report, Inventory Report, "Purchases"
#    and "Sales" grand totals) were calculated ONCE before the menu
#    loop started, so they went stale the moment you added a new
#    sale or purchase. They are now recalculated every time the menu
#    loop runs, so every screen always reflects the latest data.
# 2. Expiry tracking used two hardcoded date strings and hardcoded
#    "days remaining" numbers, so it silently stopped working for
#    any other product/date. It now works generally with datetime.
# 3. Numeric inputs (product ID, customer ID, supplier ID, quantity)
#    crashed the whole program on non-numeric input. They're now
#    guarded with try/except so a typo just prints an error instead
#    of ending the session.
# ================================================================

from datetime import datetime

EXPIRY_WARNING_DAYS = 45   # flag anything expiring within this many days


# ================================================================
# 1. BASIC INFORMATION
# ================================================================

store_name = "FreshMart Grocery Store"

current_date = "2026-08-16"

print("=" * 70)
print("             FRESHMART GROCERY MANAGEMENT SYSTEM")
print("=" * 70)


# ================================================================
# 2. CATEGORIES
# ================================================================

categories = [
    "Cooking Essentials",
    "Spices",
    "Kitchen & Pantry"
]


# ================================================================
# 3. PRODUCTS
# ================================================================

products = [
    {
        "id": 1,
        "name": "Basmati Rice",
        "category": "Cooking Essentials",
        "unit": "kg",
        "cost": 280,
        "price": 350,
        "opening_stock": 100,
        "minimum_stock": 20,
        "expiry": "2027-08-01"
    },
    {
        "id": 2,
        "name": "Wheat Flour",
        "category": "Cooking Essentials",
        "unit": "kg",
        "cost": 120,
        "price": 160,
        "opening_stock": 100,
        "minimum_stock": 20,
        "expiry": "2027-02-15"
    },
    {
        "id": 3,
        "name": "Cooking Oil",
        "category": "Cooking Essentials",
        "unit": "liter",
        "cost": 520,
        "price": 650,
        "opening_stock": 80,
        "minimum_stock": 15,
        "expiry": "2027-06-10"
    },
    {
        "id": 4,
        "name": "Sugar",
        "category": "Cooking Essentials",
        "unit": "kg",
        "cost": 145,
        "price": 180,
        "opening_stock": 100,
        "minimum_stock": 20,
        "expiry": "2027-05-20"
    },
    {
        "id": 5,
        "name": "Salt",
        "category": "Cooking Essentials",
        "unit": "kg",
        "cost": 45,
        "price": 70,
        "opening_stock": 100,
        "minimum_stock": 20,
        "expiry": "2028-01-15"
    },
    {
        "id": 6,
        "name": "Red Chili Powder",
        "category": "Spices",
        "unit": "kg",
        "cost": 650,
        "price": 800,
        "opening_stock": 70,
        "minimum_stock": 15,
        "expiry": "2027-04-10"
    },
    {
        "id": 7,
        "name": "Turmeric Powder",
        "category": "Spices",
        "unit": "kg",
        "cost": 480,
        "price": 600,
        "opening_stock": 70,
        "minimum_stock": 15,
        "expiry": "2027-04-20"
    },
    {
        "id": 8,
        "name": "Black Pepper",
        "category": "Spices",
        "unit": "kg",
        "cost": 1450,
        "price": 1800,
        "opening_stock": 30,
        "minimum_stock": 10,
        "expiry": "2027-03-10"
    },
    {
        "id": 9,
        "name": "Cumin Seeds",
        "category": "Spices",
        "unit": "kg",
        "cost": 900,
        "price": 1100,
        "opening_stock": 60,
        "minimum_stock": 15,
        "expiry": "2027-03-15"
    },
    {
        "id": 10,
        "name": "Coriander Powder",
        "category": "Spices",
        "unit": "kg",
        "cost": 550,
        "price": 700,
        "opening_stock": 60,
        "minimum_stock": 15,
        "expiry": "2027-04-01"
    },
    {
        "id": 11,
        "name": "Tea",
        "category": "Kitchen & Pantry",
        "unit": "kg",
        "cost": 1100,
        "price": 1400,
        "opening_stock": 60,
        "minimum_stock": 15,
        "expiry": "2027-07-01"
    },
    {
        "id": 12,
        "name": "Coffee",
        "category": "Kitchen & Pantry",
        "unit": "kg",
        "cost": 1800,
        "price": 2200,
        "opening_stock": 50,
        "minimum_stock": 12,
        "expiry": "2027-07-15"
    },
    {
        "id": 13,
        "name": "Milk Powder",
        "category": "Kitchen & Pantry",
        "unit": "kg",
        "cost": 950,
        "price": 1200,
        "opening_stock": 40,
        "minimum_stock": 10,
        "expiry": "2026-09-02"
    },
    {
        "id": 14,
        "name": "Tomato Ketchup",
        "category": "Kitchen & Pantry",
        "unit": "bottle",
        "cost": 280,
        "price": 350,
        "opening_stock": 40,
        "minimum_stock": 10,
        "expiry": "2026-09-08"
    },
    {
        "id": 15,
        "name": "Dishwashing Liquid",
        "category": "Kitchen & Pantry",
        "unit": "bottle",
        "cost": 220,
        "price": 300,
        "opening_stock": 50,
        "minimum_stock": 12,
        "expiry": "2027-08-10"
    }
]


# ================================================================
# 4. SUPPLIERS
# ================================================================

suppliers = [
    {
        "id": 1,
        "name": "PakFresh Wholesale",
        "phone": "0300-1111111",
        "products": [
            "Basmati Rice",
            "Wheat Flour",
            "Sugar",
            "Salt",
            "Red Chili Powder",
            "Turmeric Powder",
            "Black Pepper",
            "Cumin Seeds",
            "Coriander Powder",
            "Tea"
        ]
    },
    {
        "id": 2,
        "name": "KitchenMart Distributors",
        "phone": "0311-2222222",
        "products": [
            "Cooking Oil",
            "Tea",
            "Coffee",
            "Milk Powder",
            "Tomato Ketchup",
            "Dishwashing Liquid"
        ]
    }
]


# ================================================================
# 5. CUSTOMERS - 55
# ================================================================

customer_names = [
    "Ali Khan",
    "Ahmed Raza",
    "Hamza Malik",
    "Usman Ali",
    "Bilal Ahmed",
    "Hassan Shah",
    "Ayesha Khan",
    "Fatima Noor",
    "Omar Farooq",
    "Zain Abbas",
    "Saad Ahmed",
    "Danish Ali",
    "Talha Khan",
    "Fahad Raza",
    "Asad Malik",
    "Imran Shah",
    "Salman Ahmed",
    "Waleed Khan",
    "Arslan Ali",
    "Shahzaib Raza",
    "Haris Malik",
    "Adnan Khan",
    "Noman Ahmed",
    "Yasir Shah",
    "Kamran Ali",
    "Shoaib Khan",
    "Rizwan Ahmed",
    "Muneeb Raza",
    "Adeel Malik",
    "Junaid Khan",
    "Saif Ahmed",
    "Taha Ali",
    "Huzaifa Shah",
    "Abdullah Khan",
    "Ibrahim Raza",
    "Mustafa Ahmed",
    "Maryam Khan",
    "Hira Malik",
    "Zoya Ahmed",
    "Sana Raza",
    "Maham Ali",
    "Iqra Khan",
    "Anaya Shah",
    "Laiba Ahmed",
    "Eman Raza",
    "Mehwish Khan",
    "Kiran Malik",
    "Sadia Ali",
    "Nadia Ahmed",
    "Rabia Khan",
    "Asma Raza",
    "Saira Malik",
    "Komal Ahmed",
    "Mariam Shah",
    "Areeba Khan"
]

customers = []

customer_number = 1

for name in customer_names:

    customer = {
        "id": customer_number,
        "name": name,
        "phone": "03" + str(100000000 + customer_number),
        "email": name.lower().replace(" ", ".") + "@gmail.com",
        "address": "Street " + str(customer_number) + ", Islamabad",
        "total_purchases": 0
    }

    customers.append(customer)

    customer_number = customer_number + 1


# ================================================================
# 6. PURCHASES - 24
# ================================================================

purchases = [
    {"id": "P001", "supplier": "PakFresh Wholesale", "product": "Basmati Rice", "quantity": 50, "unit_cost": 280, "date": "2026-08-01"},
    {"id": "P002", "supplier": "PakFresh Wholesale", "product": "Wheat Flour", "quantity": 50, "unit_cost": 120, "date": "2026-08-01"},
    {"id": "P003", "supplier": "KitchenMart Distributors", "product": "Cooking Oil", "quantity": 40, "unit_cost": 520, "date": "2026-08-02"},
    {"id": "P004", "supplier": "PakFresh Wholesale", "product": "Sugar", "quantity": 50, "unit_cost": 145, "date": "2026-08-02"},
    {"id": "P005", "supplier": "PakFresh Wholesale", "product": "Salt", "quantity": 40, "unit_cost": 45, "date": "2026-08-03"},
    {"id": "P006", "supplier": "PakFresh Wholesale", "product": "Red Chili Powder", "quantity": 30, "unit_cost": 650, "date": "2026-08-03"},
    {"id": "P007", "supplier": "PakFresh Wholesale", "product": "Turmeric Powder", "quantity": 30, "unit_cost": 480, "date": "2026-08-04"},
    {"id": "P008", "supplier": "PakFresh Wholesale", "product": "Black Pepper", "quantity": 15, "unit_cost": 1450, "date": "2026-08-04"},
    {"id": "P009", "supplier": "PakFresh Wholesale", "product": "Cumin Seeds", "quantity": 30, "unit_cost": 900, "date": "2026-08-05"},
    {"id": "P010", "supplier": "PakFresh Wholesale", "product": "Coriander Powder", "quantity": 30, "unit_cost": 550, "date": "2026-08-05"},
    {"id": "P011", "supplier": "KitchenMart Distributors", "product": "Tea", "quantity": 30, "unit_cost": 1100, "date": "2026-08-06"},
    {"id": "P012", "supplier": "KitchenMart Distributors", "product": "Coffee", "quantity": 25, "unit_cost": 1800, "date": "2026-08-06"},
    {"id": "P013", "supplier": "KitchenMart Distributors", "product": "Milk Powder", "quantity": 20, "unit_cost": 950, "date": "2026-08-07"},
    {"id": "P014", "supplier": "KitchenMart Distributors", "product": "Tomato Ketchup", "quantity": 20, "unit_cost": 280, "date": "2026-08-07"},
    {"id": "P015", "supplier": "KitchenMart Distributors", "product": "Dishwashing Liquid", "quantity": 30, "unit_cost": 220, "date": "2026-08-08"},
    {"id": "P016", "supplier": "PakFresh Wholesale", "product": "Basmati Rice", "quantity": 40, "unit_cost": 280, "date": "2026-08-08"},
    {"id": "P017", "supplier": "PakFresh Wholesale", "product": "Wheat Flour", "quantity": 40, "unit_cost": 120, "date": "2026-08-09"},
    {"id": "P018", "supplier": "KitchenMart Distributors", "product": "Cooking Oil", "quantity": 30, "unit_cost": 520, "date": "2026-08-09"},
    {"id": "P019", "supplier": "PakFresh Wholesale", "product": "Sugar", "quantity": 40, "unit_cost": 145, "date": "2026-08-10"},
    {"id": "P020", "supplier": "PakFresh Wholesale", "product": "Tea", "quantity": 25, "unit_cost": 1100, "date": "2026-08-10"},
    {"id": "P021", "supplier": "KitchenMart Distributors", "product": "Coffee", "quantity": 20, "unit_cost": 1800, "date": "2026-08-11"},
    {"id": "P022", "supplier": "KitchenMart Distributors", "product": "Milk Powder", "quantity": 15, "unit_cost": 950, "date": "2026-08-12"},
    {"id": "P023", "supplier": "KitchenMart Distributors", "product": "Tomato Ketchup", "quantity": 15, "unit_cost": 280, "date": "2026-08-13"},
    {"id": "P024", "supplier": "KitchenMart Distributors", "product": "Dishwashing Liquid", "quantity": 20, "unit_cost": 220, "date": "2026-08-14"}
]


# ================================================================
# 7. SALES - 60
# ================================================================

sales = []

sale_products = [
    "Basmati Rice",
    "Wheat Flour",
    "Cooking Oil",
    "Sugar",
    "Salt",
    "Red Chili Powder",
    "Turmeric Powder",
    "Black Pepper",
    "Cumin Seeds",
    "Coriander Powder",
    "Tea",
    "Coffee",
    "Milk Powder",
    "Tomato Ketchup",
    "Dishwashing Liquid"
]

sale_quantities = [
    2, 3, 1, 4, 2,
    1, 2, 1, 2, 3,
    2, 1, 1, 2, 1
]

sale_number = 1

for i in range(60):

    product_name = sale_products[i % 15]
    quantity = sale_quantities[i % 15]

    product_price = 0

    for product in products:
        if product["name"] == product_name:
            product_price = product["price"]

    customer = customers[i % 55]

    sales.append(
        {
            "id": "S" + str(sale_number).zfill(3),
            "customer_id": customer["id"],
            "customer": customer["name"],
            "product": product_name,
            "quantity": quantity,
            "selling_price": product_price,
            "total": quantity * product_price,
            "date": "2026-08-" + str((i % 15) + 1).zfill(2)
        }
    )

    sale_number = sale_number + 1


# ================================================================
# 8. RETURNS - 10
# ================================================================

returns = [
    {
        "id": "R001",
        "sale_id": "S004",
        "customer": "Ali Khan",
        "product": "Sugar",
        "quantity": 1,
        "reason": "Damaged",
        "refund": 180
    },
    {
        "id": "R002",
        "sale_id": "S009",
        "customer": "Ahmed Raza",
        "product": "Cumin Seeds",
        "quantity": 1,
        "reason": "Wrong Item",
        "refund": 1100
    },
    {
        "id": "R003",
        "sale_id": "S014",
        "customer": "Hamza Malik",
        "product": "Tomato Ketchup",
        "quantity": 1,
        "reason": "Damaged",
        "refund": 350
    },
    {
        "id": "R004",
        "sale_id": "S019",
        "customer": "Usman Ali",
        "product": "Cooking Oil",
        "quantity": 1,
        "reason": "Damaged",
        "refund": 650
    },
    {
        "id": "R005",
        "sale_id": "S024",
        "customer": "Bilal Ahmed",
        "product": "Tea",
        "quantity": 1,
        "reason": "Customer Return",
        "refund": 1400
    },
    {
        "id": "R006",
        "sale_id": "S029",
        "customer": "Hassan Shah",
        "product": "Wheat Flour",
        "quantity": 1,
        "reason": "Wrong Item",
        "refund": 160
    },
    {
        "id": "R007",
        "sale_id": "S034",
        "customer": "Ayesha Khan",
        "product": "Black Pepper",
        "quantity": 1,
        "reason": "Damaged",
        "refund": 1800
    },
    {
        "id": "R008",
        "sale_id": "S039",
        "customer": "Fatima Noor",
        "product": "Coffee",
        "quantity": 1,
        "reason": "Customer Return",
        "refund": 2200
    },
    {
        "id": "R009",
        "sale_id": "S044",
        "customer": "Omar Farooq",
        "product": "Milk Powder",
        "quantity": 1,
        "reason": "Damaged",
        "refund": 1200
    },
    {
        "id": "R010",
        "sale_id": "S049",
        "customer": "Zain Abbas",
        "product": "Dishwashing Liquid",
        "quantity": 1,
        "reason": "Wrong Item",
        "refund": 300
    }
]


# ================================================================
# 9. STOCK TRANSFERS - 4
# ================================================================

stock_transfers = [
    {
        "id": "T001",
        "product": "Basmati Rice",
        "quantity": 20,
        "from": "Main Warehouse",
        "to": "Branch A",
        "status": "Completed"
    },
    {
        "id": "T002",
        "product": "Cooking Oil",
        "quantity": 10,
        "from": "Main Warehouse",
        "to": "Branch B",
        "status": "Completed"
    },
    {
        "id": "T003",
        "product": "Tea",
        "quantity": 10,
        "from": "Main Warehouse",
        "to": "Branch A",
        "status": "Completed"
    },
    {
        "id": "T004",
        "product": "Sugar",
        "quantity": 15,
        "from": "Branch A",
        "to": "Branch B",
        "status": "Completed"
    }
]


# ================================================================
# 10. EXPENSES
# ================================================================

expenses = [
    {"name": "Shop Rent", "amount": 25000},
    {"name": "Electricity", "amount": 8500},
    {"name": "Employee Salaries", "amount": 30000},
    {"name": "Transportation", "amount": 5000},
    {"name": "Maintenance", "amount": 3000},
    {"name": "Internet", "amount": 2500},
    {"name": "Miscellaneous", "amount": 2000}
]


# ================================================================
# 11. MAIN MENU
# ================================================================
# NOTE: Every total below (purchase cost, sales revenue, refunds,
# profit, current stock, low-stock list, expiring list, customer
# totals...) is recalculated HERE, at the top of the loop, on every
# single pass. That is the key fix: previously these were worked
# out once before the loop started, so anything added later
# (choice 16 / 17) never showed up in the Dashboard, Profit & Loss,
# Low Stock Alerts, Sales Analytics or Financial Report. Now they
# are always in sync with the current products/sales/purchases data.

while True:

    # ------------------------------------------------------------
    # RECALCULATE: CURRENT STOCK PER PRODUCT
    # ------------------------------------------------------------

    for product in products:

        purchase_quantity = 0
        sold_quantity = 0
        returned_quantity = 0
        outgoing_transfer = 0
        incoming_transfer = 0

        for purchase in purchases:

            if purchase["product"] == product["name"]:

                purchase_quantity = purchase_quantity + purchase["quantity"]

        for sale in sales:

            if sale["product"] == product["name"]:

                sold_quantity = sold_quantity + sale["quantity"]

        for returned in returns:

            if returned["product"] == product["name"]:

                returned_quantity = returned_quantity + returned["quantity"]

        for transfer in stock_transfers:

            if transfer["product"] == product["name"]:

                if transfer["from"] == "Main Warehouse":

                    outgoing_transfer = outgoing_transfer + transfer["quantity"]

                if transfer["to"] == "Main Warehouse":

                    incoming_transfer = incoming_transfer + transfer["quantity"]

        current_stock = (
            product["opening_stock"]
            + purchase_quantity
            - sold_quantity
            + returned_quantity
            - outgoing_transfer
            + incoming_transfer
        )

        product["purchase_quantity"] = purchase_quantity
        product["sold_quantity"] = sold_quantity
        product["returned_quantity"] = returned_quantity
        product["current_stock"] = current_stock


    # ------------------------------------------------------------
    # RECALCULATE: CUSTOMER TOTAL PURCHASES
    # ------------------------------------------------------------

    for customer in customers:

        customer_total = 0

        for sale in sales:

            if sale["customer_id"] == customer["id"]:

                customer_total = customer_total + sale["total"]

        customer["total_purchases"] = customer_total


    # ------------------------------------------------------------
    # RECALCULATE: PURCHASE COST / SALES REVENUE / REFUNDS
    # ------------------------------------------------------------

    total_purchase_cost = 0

    for purchase in purchases:

        purchase_total = purchase["quantity"] * purchase["unit_cost"]

        total_purchase_cost = total_purchase_cost + purchase_total

    total_sales_revenue = 0

    for sale in sales:

        total_sales_revenue = total_sales_revenue + sale["total"]

    total_refunds = 0

    for returned in returns:

        total_refunds = total_refunds + returned["refund"]

    net_revenue = total_sales_revenue - total_refunds


    # ------------------------------------------------------------
    # RECALCULATE: COST OF GOODS SOLD / PROFIT
    # ------------------------------------------------------------

    total_cogs = 0

    for sale in sales:

        product_cost = 0

        for product in products:

            if product["name"] == sale["product"]:
                product_cost = product["cost"]

        total_cogs = total_cogs + (product_cost * sale["quantity"])

    returned_cogs = 0

    for returned in returns:

        product_cost = 0

        for product in products:

            if product["name"] == returned["product"]:
                product_cost = product["cost"]

        returned_cogs = returned_cogs + (product_cost * returned["quantity"])

    net_cogs = total_cogs - returned_cogs

    gross_profit = net_revenue - net_cogs

    total_expenses = 0

    for expense in expenses:

        total_expenses = total_expenses + expense["amount"]

    net_profit = gross_profit - total_expenses


    # ------------------------------------------------------------
    # RECALCULATE: LOW STOCK ALERTS
    # ------------------------------------------------------------

    low_stock_products = []

    for product in products:

        if product["current_stock"] <= product["minimum_stock"]:

            low_stock_products.append(product)


    # ------------------------------------------------------------
    # RECALCULATE: EXPIRY TRACKING (general, not hardcoded dates)
    # ------------------------------------------------------------

    current_date_obj = datetime.strptime(current_date, "%Y-%m-%d")

    expiring_products = []

    for product in products:

        expiry_date_obj = datetime.strptime(product["expiry"], "%Y-%m-%d")

        days_remaining = (expiry_date_obj - current_date_obj).days

        product["days_remaining"] = days_remaining

        if days_remaining <= EXPIRY_WARNING_DAYS:

            expiring_products.append(product)


    # ============================================================
    # MENU
    # ============================================================

    print("\n")
    print("=" * 70)
    print("             FRESHMART MANAGEMENT SYSTEM")
    print("=" * 70)

    print("1.  Dashboard")
    print("2.  Products")
    print("3.  Categories")
    print("4.  Suppliers")
    print("5.  Customers")
    print("6.  Purchases")
    print("7.  Sales")
    print("8.  Returns")
    print("9.  Stock Transfers")
    print("10. Low Stock Alerts")
    print("11. Expiry Tracking")
    print("12. Profit & Loss")
    print("13. Sales Analytics")
    print("14. Reports")
    print("15. Search Product")
    print("16. Add New Sale")
    print("17. Add New Purchase")
    print("18. Chatbot Assistant")
    print("19. Exit")

    print("=" * 70)

    choice = input("Enter your choice: ")


    # ============================================================
    # DASHBOARD
    # ============================================================

    if choice == "1":

        print("\n")
        print("=" * 70)
        print("                       DASHBOARD")
        print("=" * 70)

        print("Store Name:              ", store_name)
        print("Current Date:            ", current_date)
        print("-" * 70)

        print("Total Products:          ", len(products))
        print("Total Categories:        ", len(categories))
        print("Total Suppliers:         ", len(suppliers))
        print("Total Customers:         ", len(customers))
        print("Total Purchases:         ", len(purchases))
        print("Total Sales Transactions:", len(sales))
        print("Total Returns:           ", len(returns))
        print("Stock Transfers:         ", len(stock_transfers))

        print("-" * 70)

        print("Gross Sales:             Rs.", total_sales_revenue)
        print("Refunds:                 Rs.", total_refunds)
        print("Net Revenue:             Rs.", net_revenue)
        print("Gross Profit:            Rs.", gross_profit)
        print("Operating Expenses:      Rs.", total_expenses)
        print("Net Profit:              Rs.", net_profit)

        print("-" * 70)

        print("Low Stock Alerts:        ", len(low_stock_products))
        print("Expiring Products:       ", len(expiring_products))

        print("=" * 70)


    # ============================================================
    # PRODUCTS
    # ============================================================

    elif choice == "2":

        print("\n")
        print("=" * 100)
        print("                         PRODUCTS")
        print("=" * 100)

        for product in products:

            print(
                product["id"],
                "|",
                product["name"],
                "|",
                product["category"],
                "|",
                "Cost:", product["cost"],
                "|",
                "Price:", product["price"],
                "|",
                "Stock:", product["current_stock"],
                "|",
                "Expiry:", product["expiry"]
            )

        print("=" * 100)


    # ============================================================
    # CATEGORIES
    # ============================================================

    elif choice == "3":

        print("\n")
        print("=" * 70)
        print("                       CATEGORIES")
        print("=" * 70)

        for category in categories:

            print("\n" + category)

            product_count = 0

            for product in products:

                if product["category"] == category:

                    product_count = product_count + 1

                    print(
                        "   ",
                        product_count,
                        ".",
                        product["name"]
                    )

        print("=" * 70)


    # ============================================================
    # SUPPLIERS
    # ============================================================

    elif choice == "4":

        print("\n")
        print("=" * 70)
        print("                       SUPPLIERS")
        print("=" * 70)

        for supplier in suppliers:

            print("\nSupplier ID:", supplier["id"])
            print("Name:", supplier["name"])
            print("Phone:", supplier["phone"])
            print("Products:")

            for supplier_product in supplier["products"]:

                print("   -", supplier_product)

        print("=" * 70)


    # ============================================================
    # CUSTOMERS
    # ============================================================

    elif choice == "5":

        print("\n")
        print("=" * 110)
        print("                         CUSTOMERS")
        print("=" * 110)

        for customer in customers:

            print(
                customer["id"],
                "|",
                customer["name"],
                "|",
                customer["phone"],
                "|",
                customer["email"],
                "|",
                "Purchases: Rs.",
                customer["total_purchases"]
            )

        print("=" * 110)


    # ============================================================
    # PURCHASES
    # ============================================================

    elif choice == "6":

        print("\n")
        print("=" * 100)
        print("                         PURCHASES")
        print("=" * 100)

        for purchase in purchases:

            total = purchase["quantity"] * purchase["unit_cost"]

            print(
                purchase["id"],
                "|",
                purchase["supplier"],
                "|",
                purchase["product"],
                "| Qty:",
                purchase["quantity"],
                "| Cost:",
                purchase["unit_cost"],
                "| Total:",
                total,
                "|",
                purchase["date"]
            )

        print("-" * 100)
        print("TOTAL PURCHASE COST: Rs.", total_purchase_cost)
        print("=" * 100)


    # ============================================================
    # SALES
    # ============================================================

    elif choice == "7":

        print("\n")
        print("=" * 110)
        print("                           SALES")
        print("=" * 110)

        for sale in sales:

            print(
                sale["id"],
                "|",
                sale["customer"],
                "|",
                sale["product"],
                "| Qty:",
                sale["quantity"],
                "| Price:",
                sale["selling_price"],
                "| Total:",
                sale["total"],
                "|",
                sale["date"]
            )

        print("-" * 110)
        print("TOTAL SALES REVENUE: Rs.", total_sales_revenue)
        print("=" * 110)


    # ============================================================
    # RETURNS
    # ============================================================

    elif choice == "8":

        print("\n")
        print("=" * 100)
        print("                         RETURNS")
        print("=" * 100)

        for returned in returns:

            print(
                returned["id"],
                "| Sale:",
                returned["sale_id"],
                "| Customer:",
                returned["customer"],
                "| Product:",
                returned["product"],
                "| Qty:",
                returned["quantity"],
                "| Reason:",
                returned["reason"],
                "| Refund:",
                returned["refund"]
            )

        print("-" * 100)
        print("TOTAL REFUNDS: Rs.", total_refunds)
        print("=" * 100)


    # ============================================================
    # STOCK TRANSFERS
    # ============================================================

    elif choice == "9":

        print("\n")
        print("=" * 100)
        print("                       STOCK TRANSFERS")
        print("=" * 100)

        for transfer in stock_transfers:

            print(
                transfer["id"],
                "|",
                transfer["product"],
                "| Qty:",
                transfer["quantity"],
                "| From:",
                transfer["from"],
                "| To:",
                transfer["to"],
                "| Status:",
                transfer["status"]
            )

        print("=" * 100)


    # ============================================================
    # LOW STOCK ALERTS
    # ============================================================

    elif choice == "10":

        print("\n")
        print("=" * 80)
        print("                       LOW STOCK ALERTS")
        print("=" * 80)

        if len(low_stock_products) == 0:

            print("No low-stock products.")

        else:

            for product in low_stock_products:

                print("⚠ LOW STOCK")
                print("Product:", product["name"])
                print("Current Stock:", product["current_stock"])
                print("Minimum Stock:", product["minimum_stock"])
                print("Status: REORDER REQUIRED")
                print("-" * 50)

        print("=" * 80)


    # ============================================================
    # EXPIRY TRACKING
    # ============================================================

    elif choice == "11":

        print("\n")
        print("=" * 80)
        print("                       EXPIRY TRACKING")
        print("=" * 80)

        if len(expiring_products) == 0:

            print("Nothing is expiring in the next", EXPIRY_WARNING_DAYS, "days.")

        else:

            for product in expiring_products:

                print("⚠ EXPIRING SOON")
                print("Product:", product["name"])
                print("Expiry:", product["expiry"])
                print("Days Remaining:", product["days_remaining"])
                print("-" * 50)

        print("=" * 80)


    # ============================================================
    # PROFIT & LOSS
    # ============================================================

    elif choice == "12":

        print("\n")
        print("=" * 70)
        print("                       PROFIT & LOSS")
        print("=" * 70)

        print("Gross Sales Revenue:       Rs.", total_sales_revenue)
        print("Less: Customer Refunds:    Rs.", total_refunds)
        print("-" * 70)

        print("Net Revenue:               Rs.", net_revenue)
        print("Cost of Goods Sold:        Rs.", net_cogs)
        print("-" * 70)

        print("Gross Profit:              Rs.", gross_profit)

        print("\nOPERATING EXPENSES")
        print("-" * 70)

        for expense in expenses:

            print(
                expense["name"],
                ": Rs.",
                expense["amount"]
            )

        print("-" * 70)

        print("Total Expenses:            Rs.", total_expenses)
        print("Net Profit:                Rs.", net_profit)

        print("=" * 70)


    # ============================================================
    # SALES ANALYTICS
    # ============================================================

    elif choice == "13":

        print("\n")
        print("=" * 90)
        print("                       SALES ANALYTICS")
        print("=" * 90)

        print("Total Transactions:", len(sales))
        print("Gross Revenue: Rs.", total_sales_revenue)
        print("Refunds: Rs.", total_refunds)
        print("Net Revenue: Rs.", net_revenue)

        print("\nPRODUCT PERFORMANCE")
        print("-" * 90)

        product_sales = []

        for product in products:

            quantity_sold = 0
            revenue = 0

            for sale in sales:

                if sale["product"] == product["name"]:

                    quantity_sold = quantity_sold + sale["quantity"]
                    revenue = revenue + sale["total"]

            product_sales.append(
                {
                    "product": product["name"],
                    "quantity": quantity_sold,
                    "revenue": revenue
                }
            )

            print(
                product["name"],
                "| Units Sold:",
                quantity_sold,
                "| Revenue: Rs.",
                revenue
            )

        print("-" * 90)

        best_product = product_sales[0]

        for item in product_sales:

            if item["revenue"] > best_product["revenue"]:

                best_product = item

        worst_product = product_sales[0]

        for item in product_sales:

            if item["revenue"] < worst_product["revenue"]:

                worst_product = item

        print("BEST SELLING PRODUCT:")
        print(best_product["product"])
        print("Revenue: Rs.", best_product["revenue"])

        print("\nLOWEST SELLING PRODUCT:")
        print(worst_product["product"])
        print("Revenue: Rs.", worst_product["revenue"])

        print("=" * 90)


    # ============================================================
    # REPORTS
    # ============================================================

    elif choice == "14":

        print("\n")
        print("=" * 70)
        print("                         REPORTS")
        print("=" * 70)

        print("1. Inventory Report")
        print("2. Sales Report")
        print("3. Purchase Report")
        print("4. Customer Report")
        print("5. Financial Report")

        report_choice = input("Select report: ")


        # --------------------------------------------------------
        # INVENTORY REPORT
        # --------------------------------------------------------

        if report_choice == "1":

            print("\n")
            print("=" * 90)
            print("                     INVENTORY REPORT")
            print("=" * 90)

            for product in products:

                print(
                    product["name"],
                    "| Opening:",
                    product["opening_stock"],
                    "| Purchased:",
                    product["purchase_quantity"],
                    "| Sold:",
                    product["sold_quantity"],
                    "| Returned:",
                    product["returned_quantity"],
                    "| Current:",
                    product["current_stock"]
                )

            print("=" * 90)


        # --------------------------------------------------------
        # SALES REPORT
        # --------------------------------------------------------

        elif report_choice == "2":

            print("\n")
            print("=" * 100)
            print("                       SALES REPORT")
            print("=" * 100)

            for sale in sales:

                print(
                    sale["id"],
                    "|",
                    sale["date"],
                    "|",
                    sale["customer"],
                    "|",
                    sale["product"],
                    "|",
                    sale["quantity"],
                    "| Rs.",
                    sale["total"]
                )

            print("=" * 100)


        # --------------------------------------------------------
        # PURCHASE REPORT
        # --------------------------------------------------------

        elif report_choice == "3":

            print("\n")
            print("=" * 100)
            print("                     PURCHASE REPORT")
            print("=" * 100)

            for purchase in purchases:

                total = (
                    purchase["quantity"]
                    * purchase["unit_cost"]
                )

                print(
                    purchase["id"],
                    "|",
                    purchase["date"],
                    "|",
                    purchase["supplier"],
                    "|",
                    purchase["product"],
                    "| Qty:",
                    purchase["quantity"],
                    "| Total:",
                    total
                )

            print("=" * 100)


        # --------------------------------------------------------
        # CUSTOMER REPORT
        # --------------------------------------------------------

        elif report_choice == "4":

            print("\n")
            print("=" * 90)
            print("                     CUSTOMER REPORT")
            print("=" * 90)

            for customer in customers:

                print(
                    customer["id"],
                    "|",
                    customer["name"],
                    "| Total Purchases: Rs.",
                    customer["total_purchases"]
                )

            print("=" * 90)


        # --------------------------------------------------------
        # FINANCIAL REPORT
        # --------------------------------------------------------

        elif report_choice == "5":

            print("\n")
            print("=" * 70)
            print("                    FINANCIAL REPORT")
            print("=" * 70)

            print("Gross Revenue:       Rs.", total_sales_revenue)
            print("Refunds:             Rs.", total_refunds)
            print("Net Revenue:         Rs.", net_revenue)
            print("COGS:                Rs.", net_cogs)
            print("Gross Profit:        Rs.", gross_profit)
            print("Expenses:            Rs.", total_expenses)
            print("Net Profit:          Rs.", net_profit)

            print("=" * 70)

        else:

            print("Invalid report choice.")


    # ============================================================
    # SEARCH PRODUCT
    # ============================================================

    elif choice == "15":

        print("\n")
        search = input("Enter product name to search: ")

        found = False

        for product in products:

            if search.lower() in product["name"].lower():

                print("\nProduct Found")
                print("-" * 50)
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Category:", product["category"])
                print("Cost Price:", product["cost"])
                print("Selling Price:", product["price"])
                print("Current Stock:", product["current_stock"])
                print("Minimum Stock:", product["minimum_stock"])
                print("Expiry:", product["expiry"])

                found = True

        if found == False:

            print("Product not found.")


    # ============================================================
    # ADD NEW SALE
    # ============================================================

    elif choice == "16":

        print("\n")
        print("=" * 70)
        print("                       NEW SALE")
        print("=" * 70)

        print("Available Products:")

        for product in products:

            print(
                product["id"],
                "-",
                product["name"],
                "| Stock:",
                product["current_stock"],
                "| Price:",
                product["price"]
            )

        # --- guarded numeric input: was int(input(...)) with no
        # try/except before, so a typo here crashed the program ---

        try:
            product_id = int(input("\nEnter Product ID: "))
        except ValueError:
            product_id = None
            print("Please enter a valid numeric Product ID.")

        if product_id is not None:

            selected_product = ""

            for product in products:

                if product["id"] == product_id:

                    selected_product = product

            if selected_product == "":

                print("Invalid Product ID.")

            else:

                print("\nAvailable Customers:")

                for customer in customers:

                    print(
                        customer["id"],
                        "-",
                        customer["name"]
                    )

                try:
                    customer_id = int(input("Enter Customer ID: "))
                except ValueError:
                    customer_id = None
                    print("Please enter a valid numeric Customer ID.")

                if customer_id is not None:

                    selected_customer = ""

                    for customer in customers:

                        if customer["id"] == customer_id:

                            selected_customer = customer

                    if selected_customer == "":

                        print("Invalid Customer ID.")

                    else:

                        try:
                            quantity = int(input("Enter Quantity: "))
                        except ValueError:
                            quantity = None
                            print("Please enter a valid numeric quantity.")

                        if quantity is not None:

                            if quantity <= 0:

                                print("Quantity must be greater than zero.")

                            elif quantity > selected_product["current_stock"]:

                                print("Not enough stock available.")

                            else:

                                total = (
                                    quantity
                                    * selected_product["price"]
                                )

                                new_sale_id = "S" + str(len(sales) + 1).zfill(3)

                                new_sale = {
                                    "id": new_sale_id,
                                    "customer_id": selected_customer["id"],
                                    "customer": selected_customer["name"],
                                    "product": selected_product["name"],
                                    "quantity": quantity,
                                    "selling_price": selected_product["price"],
                                    "total": total,
                                    "date": current_date
                                }

                                sales.append(new_sale)

                                selected_product["current_stock"] = (
                                    selected_product["current_stock"]
                                    - quantity
                                )

                                selected_customer["total_purchases"] = (
                                    selected_customer["total_purchases"]
                                    + total
                                )

                                print("\n")
                                print("=" * 60)
                                print("             SALE COMPLETED")
                                print("=" * 60)
                                print("Sale ID:", new_sale_id)
                                print("Customer:", selected_customer["name"])
                                print("Product:", selected_product["name"])
                                print("Quantity:", quantity)
                                print("Price:", selected_product["price"])
                                print("Total: Rs.", total)
                                print("Remaining Stock:", selected_product["current_stock"])
                                print("=" * 60)


    # ============================================================
    # ADD NEW PURCHASE
    # ============================================================

    elif choice == "17":

        print("\n")
        print("=" * 70)
        print("                    NEW PURCHASE")
        print("=" * 70)

        print("Available Products:")

        for product in products:

            print(
                product["id"],
                "-",
                product["name"],
                "| Cost:",
                product["cost"]
            )

        try:
            product_id = int(input("\nEnter Product ID: "))
        except ValueError:
            product_id = None
            print("Please enter a valid numeric Product ID.")

        if product_id is not None:

            selected_product = ""

            for product in products:

                if product["id"] == product_id:

                    selected_product = product

            if selected_product == "":

                print("Invalid Product ID.")

            else:

                print("\nSuppliers:")

                for supplier in suppliers:

                    print(
                        supplier["id"],
                        "-",
                        supplier["name"]
                    )

                try:
                    supplier_id = int(input("Enter Supplier ID: "))
                except ValueError:
                    supplier_id = None
                    print("Please enter a valid numeric Supplier ID.")

                if supplier_id is not None:

                    selected_supplier = ""

                    for supplier in suppliers:

                        if supplier["id"] == supplier_id:

                            selected_supplier = supplier

                    if selected_supplier == "":

                        print("Invalid Supplier ID.")

                    else:

                        try:
                            quantity = int(input("Enter Quantity: "))
                        except ValueError:
                            quantity = None
                            print("Please enter a valid numeric quantity.")

                        if quantity is not None:

                            if quantity <= 0:

                                print("Quantity must be greater than zero.")

                            else:

                                new_purchase_id = (
                                    "P"
                                    + str(len(purchases) + 1).zfill(3)
                                )

                                new_purchase = {
                                    "id": new_purchase_id,
                                    "supplier": selected_supplier["name"],
                                    "product": selected_product["name"],
                                    "quantity": quantity,
                                    "unit_cost": selected_product["cost"],
                                    "date": current_date
                                }

                                purchases.append(new_purchase)

                                selected_product["current_stock"] = (
                                    selected_product["current_stock"]
                                    + quantity
                                )

                                purchase_total = (
                                    quantity
                                    * selected_product["cost"]
                                )

                                print("\n")
                                print("=" * 60)
                                print("             PURCHASE COMPLETED")
                                print("=" * 60)
                                print("Purchase ID:", new_purchase_id)
                                print("Supplier:", selected_supplier["name"])
                                print("Product:", selected_product["name"])
                                print("Quantity:", quantity)
                                print("Unit Cost:", selected_product["cost"])
                                print("Total Cost: Rs.", purchase_total)
                                print("New Stock:", selected_product["current_stock"])
                                print("=" * 60)


    # ============================================================
    # EXIT
    # ============================================================

    # ============================================================
    # CHATBOT ASSISTANT
    # ============================================================

    elif choice == "18":

        print("\n")
        print("=" * 70)
        print("                 FRESHMART CHATBOT ASSISTANT")
        print("=" * 70)
        print("Ask me about products, stock, prices, suppliers, sales,")
        print("expiry dates, low stock, profits, or the store.")
        print("Type 'help' for examples or 'exit' to return to the menu.")
        print("=" * 70)

        while True:

            user_message = input("\nYou: ").strip().lower()

            if user_message == "exit":
                print("Bot: Returning to the main menu.")
                break

            elif user_message == "help":
                print("\nBot: You can ask things like:")
                print("- What is the price of rice?")
                print("- How much rice is in stock?")
                print("- Which products are low in stock?")
                print("- Which products are expiring soon?")
                print("- Who supplies coffee?")
                print("- What is the total sales revenue?")
                print("- What is the net profit?")
                print("- Show me product information for sugar.")

            elif "hello" in user_message or "hi" in user_message or "hey" in user_message:
                print("Bot: Hello! I am the FreshMart Assistant. How can I help you?")

            elif "store" in user_message or "shop" in user_message:
                print("Bot: The store is", store_name + ".")
                print("Bot: We currently have", len(products), "products,", len(categories),
                      "categories,", len(suppliers), "suppliers and", len(customers), "customers.")

            elif "low stock" in user_message or "low-stock" in user_message or "reorder" in user_message:
                if len(low_stock_products) == 0:
                    print("Bot: Good news. There are no low-stock products.")
                else:
                    print("Bot: These products need attention:")
                    for product in low_stock_products:
                        print("-", product["name"], "| Current Stock:",
                              product["current_stock"], "| Minimum:",
                              product["minimum_stock"])

            elif "expir" in user_message:
                if len(expiring_products) == 0:
                    print("Bot: No products are expiring within",
                          EXPIRY_WARNING_DAYS, "days.")
                else:
                    print("Bot: Products expiring within", EXPIRY_WARNING_DAYS, "days:")
                    for product in expiring_products:
                        print("-", product["name"], "| Expiry:",
                              product["expiry"], "| Days Remaining:",
                              product["days_remaining"])

            elif ("profit" in user_message or "p&l" in user_message
                  or "pnl" in user_message):
                print("Bot: Gross Profit is Rs.", gross_profit)
                print("Bot: Total Expenses are Rs.", total_expenses)
                print("Bot: Net Profit is Rs.", net_profit)

            elif ("revenue" in user_message or "sales revenue" in user_message
                  or "total sales" in user_message):
                print("Bot: Gross Sales Revenue is Rs.", total_sales_revenue)
                print("Bot: Refunds are Rs.", total_refunds)
                print("Bot: Net Revenue is Rs.", net_revenue)

            elif "refund" in user_message or "return" in user_message:
                print("Bot: Total refunds are Rs.", total_refunds)
                print("Bot: There are", len(returns), "recorded returns.")

            elif "expense" in user_message or "expenses" in user_message:
                print("Bot: Total operating expenses are Rs.", total_expenses)
                print("Bot: Main expenses include:")
                for expense in expenses:
                    print("-", expense["name"], ": Rs.", expense["amount"])

            elif "supplier" in user_message:
                supplier_found = False

                for supplier in suppliers:
                    if supplier["name"].lower() in user_message:
                        supplier_found = True
                        print("Bot:", supplier["name"], "supplies:")
                        for supplier_product in supplier["products"]:
                            print("-", supplier_product)

                for product in products:
                    if product["name"].lower() in user_message:
                        supplier_found = True
                        print("Bot: Suppliers for", product["name"] + ":")
                        for supplier in suppliers:
                            if product["name"] in supplier["products"]:
                                print("-", supplier["name"], "| Phone:", supplier["phone"])

                if supplier_found == False:
                    print("Bot: Available suppliers are:")
                    for supplier in suppliers:
                        print("-", supplier["name"], "| Phone:", supplier["phone"])

            else:
                product_found = False

                for product in products:

                    if product["name"].lower() in user_message:

                        product_found = True

                        if "price" in user_message or "cost" in user_message:
                            print("Bot:", product["name"], "costs Rs.", product["cost"],
                                  "and sells for Rs.", product["price"])

                        elif "stock" in user_message or "available" in user_message:
                            print("Bot:", product["name"], "has", product["current_stock"],
                                  product["unit"], "in stock.")
                            print("Bot: Minimum stock level is", product["minimum_stock"],
                                  product["unit"] + ".")

                        elif "expiry" in user_message or "expire" in user_message:
                            print("Bot:", product["name"], "expires on",
                                  product["expiry"], "with", product["days_remaining"],
                                  "days remaining.")

                        elif "category" in user_message:
                            print("Bot:", product["name"], "belongs to the",
                                  product["category"], "category.")

                        elif "sell" in user_message or "sold" in user_message:
                            print("Bot:", product["name"], "has sold",
                                  product["sold_quantity"], product["unit"] + ".")

                        else:
                            print("Bot: Here is the information for", product["name"] + ":")
                            print("  Category:", product["category"])
                            print("  Cost Price: Rs.", product["cost"])
                            print("  Selling Price: Rs.", product["price"])
                            print("  Current Stock:", product["current_stock"], product["unit"])
                            print("  Minimum Stock:", product["minimum_stock"], product["unit"])
                            print("  Expiry:", product["expiry"])

                if product_found == False:
                    print("Bot: I can answer questions about FreshMart products,")
                    print("stock, prices, suppliers, sales, returns, expiry,")
                    print("expenses and profits. Type 'help' for examples.")

    # ============================================================
    # EXIT
    # ============================================================

    elif choice == "19":

        print("\n")
        print("=" * 70)
        print("Thank you for using FreshMart Grocery Management System.")
        print("System shutting down...")
        print("=" * 70)

        break


    # ============================================================
    # INVALID OPTION
    # ============================================================

    else:

        print("\nInvalid choice.")
        print("Please select a number from 1 to 19.")

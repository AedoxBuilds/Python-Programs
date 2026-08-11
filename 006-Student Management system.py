def student_management_system():
    # Part 5: while Loop (runs until the user decides to stop)
    while True:
        # Part 1: Variables & Input
        name = input("Enter Student Name (or type 'exit' to quit): ").strip()

        # Part 6: break
        if name.lower() == 'exit':
            break

        # Part 7: continue
        if name == "":
            print("Name cannot be empty.")
            continue

        # Gathering the rest of the inputs and converting them to Integer/Float
        try:
            age = int(input("Enter Student Age: "))
            marks = float(input("Enter Student Marks: "))
        except ValueError:
            print("Please enter valid numbers for Age and Marks.")
            print("====================")
            continue

        # Part 2: Conditions
        passed = True

        if marks >= 90:
            print("Grade A")
        elif marks >= 80:
            print("Grade B")
        elif marks >= 70:
            print("Grade C")
        elif marks >= 60:
            print("Grade D")
        else:
            print("Fail")
            passed = False  # Mark as failed for the next step

        # Part 3: Nested Condition
        if passed:
            if age >= 18:
                print("Eligible for University Admission")
            else:
                print("Not Eligible Yet")

        # Part 4: for Loop
        for _ in range(3):
            print("Generating Report...")

        # BONUS: Clean output formatting
        print("====================")

        # Part 5: while Loop Continuation / Exit
        choice = input("Do you want to enter another student? (yes/no): ").strip().lower()

        if choice == 'no' or choice == 'exit':
            break  # Stops the while loop and ends the program


# Run the program
student_management_system()


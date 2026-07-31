print("===== Student Information =====")

name = input("\nEnter Name: ")
age = int(input("Enter Age: "))
marks = int(input("Enter Marks: "))

print("\nOutput\n")

print("Name:", name)
print("Adult:", age >= 18)
print("Passed:", marks >= 50)
print("Excellent Student:", marks >= 60)

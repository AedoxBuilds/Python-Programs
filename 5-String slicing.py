website1 = "www.newspanther.co.za"
website2 = "www.newspanther.co.uk"
website3 = "www.newspanther.co.pk"

print("Choose a website:")
print("1.", website1)
print("2.", website2)
print("3.", website3)

choice = input("\nEnter your choice (1-3): ")

if choice == "1":
    print("Country Code:", website1[-2:])
    print("You selected South Africa.")

elif choice == "2":
    print("Country Code:", website2[-2:])
    print("You selected United Kingdom.")

elif choice == "3":
    print("Country Code:", website3[-2:])
    print("You selected Pakistan.")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")

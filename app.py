
from models import add_flavor

def main():
    while True:
        print("1. Add Flavor")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter flavor name: ")
            description = input("Add description: ")
            season = input("Enter season: ")
            availability = input("Is it available? (yes/no): ") == 'yes'
            add_flavor(name, description, season, availability)
            print("Flavor added successfully!")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

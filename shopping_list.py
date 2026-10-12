# shopping_list.py

# Start with an empty shopping list
shopping_list = []

# Display the menu repeatedly
while True:
    print("\nShopping List Manager")
    print("Choose: add / remove / show / done")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()if item:
            shopping_list.append(item)
            print(item, "has been added to your list.")
        else:
            print("Please enter a valid item.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please enter add, remove, show, or done.")
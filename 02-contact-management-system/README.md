# Contact Management System

**Source:** [LabEx - Python Data Structures](https://labex.io/labs/python-python-data-structures-393168?course=quick-start-with-python)

In this lab, you will explore fundamental Python data structures: lists, tuples, sets, and dictionaries. You will create a practical contact management program that demonstrates how these different structures can work together in a real-world application.

## Tasks

1. Create a new file named [`contact_manager.py`](contact_manager.py).
2. Implement the core contact logic:
   - Use a dictionary to store contact information (phone and email) mapped to names.
   - Use a set to store and manage unique "Favorite" contacts.
3. Create an interactive menu system using a `while` loop.
4. Implement the following functions:
   - `add_contact(contacts, name, phone, email)`
   - `remove_contact(contacts, name)`
   - `display_contacts(contacts)`

## Requirements

- Use a dictionary for efficient data lookup and storage of contact details.
- Utilize a set to perform operations where only unique elements are required (Favorites).
- Implement a menu-driven interface that handles user input for adding, removing, and displaying data.
- Ensure the program handles "contact not found" scenarios gracefully when removing or favoriting.

## Execution

To run the program, use the following command in your terminal:

```bash
python contact_manager.py
```
## Expected Output

```plaintext
Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 1
Enter name: Alice
Enter phone number: 123-456-7890
Enter email: alice@example.com
Contact Alice added successfully.

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 1
Enter name: Bob
Enter phone number: 987-654-3210
Enter email: bob@example.com
Contact Bob added successfully.

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 3

Contact List:
Name: Alice, Phone: 123-456-7890, Email: alice@example.com
Name: Bob, Phone: 987-654-3210, Email: bob@example.com

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 4
Enter name to add to favorites: Alice
Alice added to favorites.

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 5

Favorite Contacts:
Alice

Contact Manager
1. Add Contact
2. Remove Contact
3. Display Contacts
4. Add to Favorites
5. Display Favorites
6. Exit
Enter your choice (1-6): 6
Thank you for using Contact Manager. Goodbye!
```

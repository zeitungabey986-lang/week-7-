Week 7 Assignment: Hands-On Lab — Shopping List Manager
This repository contains my Python programs for practicing list operations and managing a shopping list.

Files
list_warmup.py — Creates a list of fruits and demonstrates indexing, appending, removing, and counting items.
shopping_list.py — Implements an interactive shopping list manager that allows users to add, remove, and display items.
list_report.py — Prints a numbered shopping list, counts item names with more than four characters, and finds the longest item name.
screenshots/ — Contains screenshots showing the output of all three Python programs.
Why is it safer to check in before calling .remove()?
Checking whether an item exists in a list before removing it prevents Python from raising a ValueError when the item is not found. This makes the program safer because it can continue running instead of crashing. It also allows the program to display a helpful message when an item is missing.

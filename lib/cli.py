#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_providers,
    list_users,
    list_bookings
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_providers()
        elif choice == "2":
            list_users()
        elif choice == "3":
            list_bookings()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all providers")
    print("2. List all users")
    print("3. List all bookings" )

if __name__ == "__main__":
    main()
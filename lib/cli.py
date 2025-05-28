#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_providers,
    find_provider_name,
    list_users,
    find_user_name,
    list_bookings,
    find_booking_location
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_providers()
        elif choice =="2":
            find_provider_name()
        elif choice == "3":
            list_users()
        elif choice == "4":
            find_user_name()
        elif choice == "5":
            list_bookings()
        elif choice == "6":
            find_booking_location()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all providers")
    print("2. Find provider by name")
    print("3. List all users")
    print("4. Find user by name")
    print("5. List all bookings" )
    print("6. Find bookings by location")

if __name__ == "__main__":
    main()
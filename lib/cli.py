#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_providers,
    find_provider_name,
    list_users,
    find_user_name,
    list_bookings,
    find_booking_location,
    list_services,
    add_user,
    add_provider,
    add_new_booking
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
        elif choice == "7":
            list_services()
        elif choice =="8":
            add_user()
        elif choice == "9":
            add_provider()
        elif choice =="10":
            add_new_booking()
        else:
            print("Invalid choice")

def menu():
    print("Hey there, welcome to Jplug !!")
    print("Please select an option to interact with the system:")
    print("0. Exit the program")
    print("1. List all providers")
    print("2. Find provider by name")
    print("3. List all users")
    print("4. Find user by name")
    print("5. List all bookings" )
    print("6. Find bookings by location")
    print("7. List all services")
    print("8. Add a new user")
    print("9. Add a new provider")
    print("10. Add a new booking")

if __name__ == "__main__":
    main()
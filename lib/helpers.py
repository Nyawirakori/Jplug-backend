from db.models import Service, Provider, User, Booking,session
from counties import valid_counties
from datetime import datetime

def exit_program():
    print("Goodbye! Thank you for using Jplug ❤ ❤︎")
    exit()

#Implementation for Services
def list_services():
    services = Service.get_services()
    service_types = [service.service_type for service in services]
    print(f"service_types {service_types}")

#Implementation for Provider
#listing all providers
def list_providers():
    providers= Provider.get_all()
    for provider in providers:
        service_type = provider.service.service_type if provider.service else "Unknown"
        print([f"Name: {provider.name}, Location: {provider.location}, Phone: {provider.phonenumber}, Price: {provider.price}, Service: {service_type}"])

#finding provider by name
def find_provider_name():
    name = input("Enter a provider's name:")
    providers = Provider.find_by_name(name)
    if providers:
        for provider in providers:
            print(provider)
    else:
        print(f"Provider {name} not found")

#Adding a new provider
def add_provider():
    name = input("Enter the provider's first and last name: ").title()
    
    # Validate location
    while True:
        location = input("Enter your county name: ").title().strip()
        if location not in valid_counties:
            print(f"'{location}' is not a valid county in Kenya. Try again.")
        else:
            break

    contact = input("Enter phone number: ")
    price = input("Enter charges: ")

    # Validate service type
    services = Service.get_services()
    service_types = [service.service_type for service in services]

    while True:
        service_input = input(f"Enter service type (options: {', '.join(service_types)}): ").title()
        matching_service = next((s for s in services if s.service_type == service_input), None)
        if matching_service:
            break
        else:
            print("Invalid service type. Try again.")

    # Create and save the provider
    new_provider = Provider(
        name=name,
        location=location,
        phonenumber=contact,
        price=float(price),
        service=matching_service
    )
    session.add(new_provider)
    session.commit()
    print(f"Provider '{new_provider.name}' added successfully!")

#deleting a provider
def delete_provider():
    pass

#Implementation for users
#listing all users
def list_users():
    users = User.get_users()
    for user in users:
        print([f"Name:{user.user_name}, location:{user.location}"])

#finding users by their user_name
def find_user_name():
    username = input("Enter a provider's name:")
    users = User.find_by_user_name(username)
    if users:
        for user in users:
            print(user)
    else:
        print(f"User {username} not found")

#Adding a new user
def add_user():
    user_name = input("Enter your first and last name: ").title()
   
    while True:
        location = input("Enter county name: ").title().strip()
        try:
            if location not in valid_counties:
                raise ValueError(f"'{location}' is not a valid county in Kenya.")
            break 
        except ValueError as e:
            print(e)  

    new_user = User(user_name=user_name, location=location)
    session.add(new_user)
    session.commit()
    print(f"User '{new_user.user_name}' added successfully!")

def delete_user():
    pass

#Implementation for bookings
#listing all bookings
def list_bookings():
    bookings = Booking.get_bookings()
    for booking in bookings:
        user_name = booking.user.user_name if booking.user else "Unknown"
        provider_name = booking.provider.name if booking.provider else "Unknown"

        print([f"{user_name} booked {provider_name} at {booking.created_at}. The status of booking is {booking.status}"])

#Finding bookings by id
def find_booking_location():
    location = input("Enter county name:")
    bookings = Booking.get_bookings()
    # Filter bookings where the related provider's location matches
    filteredbookings= [
        b for b in bookings 
        if b.provider and b.provider.location.lower() == location.lower()
    ]

    if filteredbookings:
        for booking in filteredbookings:
            user_name = booking.user.user_name if booking.user else "Unknown"
            provider_name = booking.provider.name if booking.provider else "Unknown"
            print([f"{user_name} booked {provider_name} at {booking.created_at}. Status: {booking.status}"])
    else:
        print(f"No bookings found for {location}")

#adding a new booking
from datetime import datetime
from counties import valid_counties

def add_new_booking():
    # Step 1: Select User
    users = User.get_users()
    if not users:
        print("No users found. Please add a user first.")
        return

    print("\nAvailable users:")
    for i, user in enumerate(users, 1):
        print(f"{i}. {user.user_name} ({user.location})")
    
    try:
        user_choice = int(input("Select a user by number: ")) - 1
        selected_user = users[user_choice]
    except (IndexError, ValueError):
        print("Invalid user selection.")
        return

    # Step 2: Select Service
    services = Service.get_services()
    if not services:
        print("No services available.")
        return

    print("\nAvailable services:")
    for i, service in enumerate(services, 1):
        print(f"{i}. {service.service_type}")
    
    try:
        service_choice = int(input("Select a service by number: ")) - 1
        selected_service = services[service_choice]
    except (IndexError, ValueError):
        print("Invalid service selection.")
        return

    # Step 3: Enter Location
    while True:
        location = input("Enter preffered provider's county name: ").title().strip()
        if location not in valid_counties:
            print(f"'{location}' is not a valid county in Kenya. Try again.")
        else:
            break

    # Step 4: Filter Providers by Service AND Location
    filtered_providers = [
        p for p in selected_service.providers
        if p.location.lower() == location.lower()
    ]

    if not filtered_providers:
        print(f"No providers found for {selected_service.service_type} in {location}.")
        return

    print(f"\nAvailable providers for {selected_service.service_type} in {location}:")
    for i, provider in enumerate(filtered_providers, 1):
        print(f"{i}. {provider.name} - {provider.location} (Ksh {provider.price})")

    try:
        provider_choice = int(input("Select a provider by number: ")) - 1
        selected_provider = filtered_providers[provider_choice]
    except (IndexError, ValueError):
        print("Invalid provider selection.")
        return

    # Step 5: Enter booking status
    status = input("Enter booking status: ").title()

    # Step 6: Create and save booking
    new_booking = Booking(
        created_at=datetime.now(),
        status=status,
        user=selected_user,
        provider=selected_provider
    )

    session.add(new_booking)
    session.commit()
    print(f"Booking confirmed")

#deleting bookings
def delete_booking():
    pass

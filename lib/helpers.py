from db.models import Service, Provider, User, Booking

def exit_program():
    print("Goodbye!")
    exit()

#Implementation for Services

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
from db.models import Service, Provider, User, Booking

def exit_program():
    print("Goodbye!")
    exit()

#Implementation for Provider
def list_providers():
    providers= Provider.get_all()
    for provider in providers:
        service_type = provider.service.service_type if provider.service else "Unknown"
        print([f"Name: {provider.name}, Location: {provider.location}, Phone: {provider.phonenumber}, Price: {provider.price}, Service: {service_type}"])

#Implementation for users
def list_users():
    users = User.get_users()
    for user in users:
        print([f"Name:{user.user_name}, location:{user.location}"])

#Implementation for bookings
def list_bookings():
    bookings = Booking.get_bookings()
    for booking in bookings:
        user_name = booking.user.user_name if booking.user else "Unknown"
        provider_name = booking.provider.name if booking.provider else "Unknown"

        print([f"{user_name} booked {provider_name} at {booking.created_at}. The status of booking is {booking.status}"])
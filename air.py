from datetime import datetime, timedelta

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        
class Property:
    def __init__(self, property_id, host_id, title, description, address):
        self.property_id = property_id
        self.host_id = host_id
        self.title = title
        self.description = description
        self.address = address
        self.calendar = {}
        
class Booking:
    def __init__(self, booking_id, guest_id, property_id, check_in, check_out, total_price):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.property_id = property_id
        self.check_in = check_in
        self.check_out = check_out
        self.total_price = total_price
    
    @staticmethod    
    def book_property(property, guest, check_in, check_out):
        # Convert check_in and check_out to datetime objects if they are strings
        if isinstance(check_in, str):
          check_in = datetime.strptime(check_in, '%Y-%m-%d')
        if isinstance(check_out, str):
          check_out = datetime.strptime(check_out, '%Y-%m-%d')
          
        # Check for availability
        current_date = check_in
        while current_date < check_out:
          if not property.calendar.get(current_date.strftime('%Y-%m-%d'), False): #Check for value, default to False
              return "Property not available for selected dates"
          current_date += timedelta(days=1)
        
        # Create booking object
        booking_id = generate_booking_id()
        booking = Booking(booking_id, guest.user_id, property.property_id, check_in, check_out, calculate_price(property, check_in, check_out))
        
        # Update property calender
        current_date = check_in
        while current_date < check_out:
          property.calendar[current_date.strftime('%Y-%m-%d')] = False
          current_date += timedelta(days=1)
            
        return booking
      
    @staticmethod
    def check_in(booking):
        # Implement check-in logic (e.g., send instructions, confirm identity)
        print(f"Guest {booking.guest_id} has checked in to property {booking.property_id}!")
        
    @staticmethod
    def check_out(booking, property):
        # Implement check_out logic (e.g., collect feedback,release deposit)
        print(f"Guest {booking.guest_id} has checked out of property {booking.property_id}.")
        # Mark property available again in calendar
        current_date = booking.check_in
        while current_date < booking.check_out:
          property.calendar[current_date.strftime('%Y-%m-%d')] = True
          current_date += timedelta(days=1)
          
# Dummy functions for demonstration purposes
def generate_booking_id():
  # Dummy implementation for generating a unique booking ID
  return 1

def calculate_price(property, check_in, check_out):
  # Dummy implementation for calculating the total price
  return 100
             
             
            
        
        
        

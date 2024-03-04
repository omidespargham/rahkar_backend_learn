"""
This is a code example with wrong approach.
We created this code intentionally to demonstrate facade concept in the next part
"""

class MovieDatabase:
    def __init__(self):
        self.movies = {}

    def add_movie(self, name, ticket_price):
        self.movies[name] = ticket_price

    def get_movie_ticket_price(self, name):
        return self.movies.get(name, None)

class SeatManager:
    def __init__(self):
        self.available_seats = {}

    def set_available_seats(self, movie_name, seats):
        self.available_seats[movie_name] = seats

    def get_available_seats(self, movie_name):
        return self.available_seats.get(movie_name, None)

class PaymentGateway:
    def process_payment(self, amount):
        # Simulate payment processing
        return True

class TicketBookingSystem:
    def __init__(self):
        self.movie_database = MovieDatabase()
        self.seat_manager = SeatManager()
        self.payment_gateway = PaymentGateway()

    def book_ticket(self, movie_name, num_tickets):
        ticket_price = self.movie_database.get_movie_ticket_price(movie_name)
        if ticket_price is None:
            return "Movie not found"

        available_seats = self.seat_manager.get_available_seats(movie_name)
        if available_seats is None or num_tickets > available_seats:
            return "Not enough available seats"

        total_amount = ticket_price * num_tickets
        if not self.payment_gateway.process_payment(total_amount):
            return "Payment failed"

        return f"Successfully booked {num_tickets} ticket(s) for {movie_name}"

# Client code
if __name__ == "__main__":
    booking_system = TicketBookingSystem()
    booking_system.movie_database.add_movie("Avengers: Endgame", 12)
    booking_system.seat_manager.set_available_seats("Avengers: Endgame", 100)
    result = booking_system.book_ticket("Avengers: Endgame", 3)
    print(result)



"""
This is a code example with right approach. 
we used facade concept in this code to implement one way simple interface
"""

class TicketBookingFacade:
    def __init__(self, movie_database, seat_manager, payment_gateway):
        self.movie_database = movie_database
        self.seat_manager = seat_manager
        self.payment_gateway = payment_gateway

    def reserve_ticket(self, movie_name, num_tickets, payment_info):
        movie = self.movie_database.get_movie(movie_name)
        if movie is None:
            return "Movie not found"

        available_seats = self.seat_manager.get_available_seats(movie)
        if num_tickets > available_seats:
            return "Not enough available seats"

        total_amount = movie.ticket_price * num_tickets
        success = self.payment_gateway.make_payment(payment_info, total_amount)
        if not success:
            return "Payment failed"

        booking_reference = self.seat_manager.book_seats(movie, num_tickets)
        return f"Booking successful! Reference: {booking_reference}"

class MovieDatabase:
    def get_movie(self, movie_name):
        # Query database and return movie object
        pass

class SeatManager:
    def get_available_seats(self, movie):
        # Query seat availability for given movie
        pass

    def book_seats(self, movie, num_tickets):
        # Book seats for given movie
        pass

class PaymentGateway:
    def make_payment(self, payment_info, amount):
        # Process payment
        pass

# Create objects outside of main function
movie_database = MovieDatabase()
seat_manager = SeatManager()
payment_gateway = PaymentGateway()

# Client code
if __name__ == "__main__":
    ticket_booking_facade = TicketBookingFacade(movie_database, seat_manager, payment_gateway)
    result = ticket_booking_facade.reserve_ticket("Avengers: Endgame", 3, {"card_number": "123456789", "expiry_date": "12/24", "cvv": "123"})
    print(result)









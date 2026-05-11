## Challenge: Movie Ticket Booking System (OOP)

### Description:
Create a class-based system to manage a theatre’s ticket booking. Your system should handle multiple movies, seat bookings, cancellations, and total revenue tracking. Implement proper object-oriented design principles: encapsulation, abstraction, inheritance, and method overriding where needed.
### Requirements:
1. Classes and Attributes:
  - Movie:
    - name (str): Name of the movie.
    - total_seats (int): Total seats in theatre.
    - ticket_price (float): Price per ticket.
    - booked_seats (int): Starts at 0.
  - Theatre:
    - Can store multiple Movie objects.
    - revenue (float): Total money earned from all bookings.
2. Methods:
  - Movie.book_ticket(num_tickets):
    - If enough seats are available:
      - Increase booked_seats.
      - Return the total amount to pay.
  - Else:
    - Return "Sorry, not enough seats available".
  - Movie.show_status():
    - Display movie name, seats available, and seats booked so far.
  - Theatre.add_movie(movie_obj):
    - Add a Movie object to the theatre.
  - Theatre.show_movies():
    - List all movies with available seats.
  - Theatre.book_movie_ticket(movie_name, num_tickets):
    - Book tickets for a movie by name.
    - Update the theatre’s total revenue if booking succeeds.
Extra Challenges:
      
- Prevent overbooking even when multiple threads try to book tickets simultaneously.
- Create a subclass PremiumMovie that has a surcharge per ticket and overrides book_ticket.
- Implement a cancel_ticket(num_tickets) method for Movie that decreases booked seats and refunds the theatre.
- Add validation to prevent negative ticket numbers.
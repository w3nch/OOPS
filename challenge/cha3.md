## Challenge: Library Management System (OOP)

### Description:
Create a class-based system to manage books, members, and a library. The system should handle borrowing, returning, and book availability. Implement aggregation, inheritance, and polymorphism where applicable.

### Requirements:
1. Classes and Attributes:
  - Book:
    - title (str)
    - author (str)
    - available_copies (int)
  - Member:
    - name (str)
    - borrowed_books (list of Book)
  - Library:
    - books (list of Book)
2. Methods:
  - Library.add_book(book_obj):
    - Add a Book object to the library.
  - Member.borrow_book(book_title, library_obj):
    - Borrow a book if available; update library and member records.
  - Member.return_book(book_title, library_obj):
    - Return a book and update library availability.
  - Library.show_books():
    - Display all books with available copies.

**Extra Challenges:**
- Create a subclass PremiumMember that can borrow more books than normal members.
- Track overdue books with dates.
- Implement search by author or title.

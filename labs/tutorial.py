def find_available_seats(bookings, all_seats):
    book_seats = []
    for booking in bookings:
        book_seats.append(booking[1])
    available_seats = []
    for seat in all_seats:
        if seat not in book_seats:
            available_seats.append(seat)
    return available_seats


bookings = [("Ali", 12), ("Sara", 5), ("John", 8)]
all_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(find_available_seats(bookings, all_seats))
# BookMyShow Project in Python
# Modules: random, time, datetime, pygame

import random
import time
import pygame as p
from datetime import datetime, timedelta

p.init()
p.display.set_caption("Book My Show")
ps1=p.display.set_mode((400,400))
ps=p.image.load(r"C:\Users\god\Downloads\png-clipart-bookmyshow-india-discounts-and-allowances-ticket-affiliate-marketing-india-company-text-thumbnail.jpg")
ps1.blit(ps,(10,50))
p.display.update()
time.sleep(5)
p.quit()

# Data setup
cities = {
    "1": "Mumbai",
    "2": "Delhi",
    "3": "Chennai",
    "4": "Bangalore",
    "5": "Salem"
}

movies = {
    "PVR Cinemas": ["Leo", "Jawan", "KGF 2"],
    "INOX": ["Pushpa 2", "Salaar"],
    "Cinepolis": ["Avatar 2", "Dune 2"],
    "PVR Saket": ["Animal", "Jawan"],
    "Carnival Cinemas": ["KGF 2", "Leo"],
    "AGS Cinemas": ["Pushpa 2", "Salaar"],
    "Jazz Cinemas": ["Leo", "Avatar 2"],
    "Forum Mall": ["Jawan", "KGF 2"],
    "GT World Cinemas": ["Dune 2", "Pushpa 2"],
    "ARRS Multiplex": ["Dude", "Bison"],
    "ROX DNC Theatre": ["Dies Irae", "Predator-Badlands"]
}

theaters = {
    "Mumbai": ["PVR Cinemas", "INOX", "Cinepolis"],
    "Delhi": ["PVR Saket", "Carnival Cinemas"],
    "Chennai": ["AGS Cinemas", "Jazz Cinemas"],
    "Bangalore": ["Forum Mall", "GT World Cinemas"],
    "Salem": ["ARRS Multiplex", "ROX DNC Theatre"]
}
# Generate next 5 days as show dates
show_dates = [(datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(5)]

show_times = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
screens = [1, 2, 3]

# Seat setup
def show_seats():
    print("\nAvailable Seats (O = Open, X = Booked)")
    seats = ["O"] * 30
    for i in range(0, 30, 10):
        print(" ".join(seats[i:i+10]))
    return seats

# Book seats
def book_seats(seats):
    seat_nums = input("\nEnter seat numbers to book (e.g., 5 6 7): ").split()
    for s in seat_nums:
        s = int(s)
        if 1 <= s <= 30:
            seats[s-1] = "X"
    print("\nUpdated Seat Layout:")
    for i in range(0, 30, 10):
        print(" ".join(seats[i:i+10]))
    print(f"\nSeats booked: {len(seat_nums)}")
    return len(seat_nums)

# Payment system
def payment(total):
    print("\nPayment:")
    print(" Online Payment")
    upi=int(input("Enter upi id:"))
    amount=int(input("Enter the amount:"))
    print("Processing online payment...")
    time.sleep(2)
    print("Payment Successful!")

# Main booking flow
def book_my_show():
    print("=====  Welcome to BookMyShow =====")
    # Choose city
    print("\nAvailable Cities:")
    for k, v in cities.items():
        print(f"{k}. {v}")
    city_choice = input("Enter city number: ")
    if city_choice not in cities:
        print("Invalid city choice!")
        return
    city = cities[city_choice]
    print(f"\nSelected City: {city}")

    # Choose theater
    print("\nAvailable Theaters:")
    for i, t in enumerate(theaters[city], 1):
        print(f"{i}. {t}")
    theater_choice = int(input("Enter theater number: "))
    theater = theaters[city][theater_choice - 1]
    print(f"\nSelected Theater: {theater}")

    # Choose movie
    print("\nAvailable Movies:")
    for i, m in enumerate(movies[theater], 1):
        print(f"{i}. {m}")
    movie_choice = int(input("Enter movie number: "))
    movie = movies[theater][movie_choice - 1]
    print(f"\nSelected Movie: {movie}")

    # Choose screen and time
    print("\nAvailable Screens:", screens)
    screen = random.choice(screens)
    print(f"Assigned Screen: {screen}")

    # Choose show date
    print("\nAvailable Show Dates:")
    for i, date in enumerate(show_dates, 1):
        print(f"{i}. {date}")
    date_choice = int(input("\nEnter date number: "))
    selected_date = show_dates[date_choice - 1]

    print("\nShow Timings:")
    for i, t in enumerate(show_times, 1):
        print(f"{i}. {t}")
    time_choice = int(input("Choose show time : "))
    show_time = show_times[time_choice - 1]

    print(f"\nShow Time: {show_time}")

    # Seat booking
    seats = show_seats()
    num_tickets = book_seats(seats)
    price_per_ticket = 200
    total = num_tickets * price_per_ticket

    print(f"\nAmount: Rs.{total}")

    # Payment
    payment(total)

    # Confirmation
    booking_id = random.randint(1000, 9999)

    # Confirmation
    booking_id = random.randint(1000, 9999)
    print("\n? Booking Confirmed!")
    print("----------------------------")
    print(f"City: {city}")
    print(f"Theater: {theater}")
    print(f"Movie: {movie}")
    print(f"Screen: {screen}")
    print(f"Show Time: {show_time}")
    print(f"Tickets: {num_tickets}")
    print(f"Booking ID: BMS{booking_id}")
    print("Enjoy your movie! ??")
    print("----------------------------")

book_my_show()
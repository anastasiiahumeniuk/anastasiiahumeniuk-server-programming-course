from core.repositories import HotelRepository
from datetime import date

def test_hotel_repository():
    hotel_repo = HotelRepository()

    new_guest = hotel_repo.guests.create(
        first_name="Олена",
        last_name="Петренко",
        email="olena.petrenko@mail.com",
        phone_number="+380501112233",
        passport_series="BM",
        passport_number="123432108",
        date_of_birth=date(1990, 5, 17)
    )
    print("Новий гість доданий:", new_guest)

    all_guests = hotel_repo.guests.get_all()
    print("\nВсі гості:")
    for guest in all_guests:
        print(guest)

    guest_by_id = hotel_repo.guests.get_by_id(new_guest.id)
    print("\nГість за ID:", guest_by_id)

    new_room = hotel_repo.rooms.create(
        room_number="234",
        room_type_id=1,
        floor_number=1,
        capacity=2,
        price_per_night=120.00,
        status="available"
    )
    print("\nНова кімната додана:", new_room)

    all_rooms = hotel_repo.rooms.get_all()
    print("\nВсі кімнати:")
    for room in all_rooms:
        print(room)


    new_booking = hotel_repo.bookings.create(
        guest=new_guest,
        room=new_room,
        check_in_date=date(2025, 10, 25),
        check_out_date=date(2025, 10, 30),
        total_price=600.00
    )
    print("\nНове бронювання додано:", new_booking)



    booking_by_id = hotel_repo.bookings.get_by_id(new_booking.id)
    print("\nБронювання за ID:", booking_by_id)


# python manage.py shell
#from core.custom_test import test_hotel_repository
#test_hotel_repository()



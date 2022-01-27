class Event:

    def __init__(self, date, name, number_of_guests, room_name, description, recurring):
        self.date = date
        self.name = name
        self.number_of_guests = number_of_guests
        self.room_name = room_name
        self.description = description
        self.recurring = recurring
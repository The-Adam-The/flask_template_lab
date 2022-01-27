import unittest
from modules.event import Event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.sarahs_party = Event("5/2/2022", "Sarah's Birthday Party", 10, "The Silver Suite", "Sarah's 21st Birthday Party")

    def test_object_has_date(self):
        self.assertEqual("5/2/2022", self.sarahs_party.date)

    def test_object_has_name(self):
        self.assertEqual("Sarah's Birthday Party", self.sarahs_party.name)

    def test_object_has_number_of_guests(self):
        self.assertEqual(10, self.sarahs_party.number_of_guests)

    def test_object_has_room_name(self):
        self.assertEqual("The Silver Suite", self.sarahs_party.room_name)

    def test_object_has_description(self):
        self.assertEqual("Sarah's 21st Birthday Party", self.sarahs_party.description)
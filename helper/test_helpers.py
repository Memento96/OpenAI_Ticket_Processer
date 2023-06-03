import unittest
from helpers import generate_ticket, get_location_string, get_bot_id


class TestFunctions(unittest.TestCase):

    def test_generate_ticket(self):
        ticket = generate_ticket()
        self.assertIsInstance(ticket, int)
        self.assertGreaterEqual(ticket, 0)
        self.assertLessEqual(ticket, 99999)

    def test_get_location_string(self):
        bot_api = {
            "location": {
                "lat": 37.7749,
                "lon": -122.4194
            }
        }
        location_string = get_location_string(bot_api)
        self.assertEqual(location_string, "Latitude: 37.7749, Longitude: -122.4194")

    def test_get_location_string_with_invalid_data(self):
        bot_api = {}
        location_string = get_location_string(bot_api)
        self.assertIsNone(location_string)

    def test_get_bot_id(self):
        bot_api = {
            "bot_id": "12345"
        }
        bot_id = get_bot_id(bot_api)
        self.assertEqual(bot_id, "12345")

    def test_get_bot_id_with_invalid_data(self):
        bot_api = {}
        bot_id = get_bot_id(bot_api)
        self.assertIsNone(bot_id)


if __name__ == '__main__':
    unittest.main()


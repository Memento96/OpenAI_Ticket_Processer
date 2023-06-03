import asyncio
import logging
import unittest
from data.ticket_manager import TicketManager

# Disable logging during unit tests
logging.disable(logging.CRITICAL)

class TestTicketManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the tickets list for each test case
        TicketManager.tickets = []

    def test_append_ticket(self):
        ticket = {
            "ticket_id": 1,
            "status": "open"
        }
        TicketManager.append_ticket(ticket)
        self.assertIn(ticket, TicketManager.tickets)

    def test_update_ticket(self):
        ticket = {
            "ticket_id": 2,
            "status": "open"
        }
        TicketManager.tickets.append(ticket)
        new_data = {"status": "closed"}
        TicketManager.update_ticket(ticket_id=2, new_data=new_data)
        updated_ticket = TicketManager.get_ticket_by_id(2)
        self.assertEqual(updated_ticket["status"], "closed")

    def test_get_ticket_by_id(self):
        ticket = {
            "ticket_id": 3,
            "status": "open"
        }
        TicketManager.tickets.append(ticket)
        retrieved_ticket = TicketManager.get_ticket_by_id(3)
        self.assertEqual(retrieved_ticket, ticket)

    def test_get_ticket_by_id_nonexistent(self):
        ticket = TicketManager.get_ticket_by_id(4)
        self.assertIsNone(ticket)

    def test_get_all_tickets(self):
        ticket1 = {
            "ticket_id": 5,
            "status": "open"
        }
        ticket2 = {
            "ticket_id": 6,
            "status": "closed"
        }
        TicketManager.tickets.append(ticket1)
        TicketManager.tickets.append(ticket2)
        all_tickets = TicketManager.get_all_tickets()
        self.assertIn(ticket1, all_tickets)
        self.assertIn(ticket2, all_tickets)


if __name__ == '__main__':
    unittest.main()


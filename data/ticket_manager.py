import asyncio
import logging
import time
import tracemalloc

# Enable tracemalloc
tracemalloc.start()

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)

class TicketManager:

    tickets = []

    @classmethod
    def append_ticket(cls, ticket):
        print(ticket["ticket_id"])
        cls.tickets.append(ticket)
        # cls.monitor_ticket(ticket["ticket_id"]) #TODO fix the asynchronous process to monitor the status of a ticket



    @classmethod
    def update_ticket(cls, ticket_id, new_data):
        for ticket in cls.tickets:
            if ticket['ticket_id'] == ticket_id:
                ticket.update(new_data)
                break

    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        for ticket in cls.tickets:
            if ticket['ticket_id'] == ticket_id:
                return ticket
        return None

    @classmethod
    def get_all_tickets(cls):
        return cls.tickets

    # This is the function in charge of monitoring the created tickets, as soon as the ticket is "closed" it stops
    @classmethod
    async def monitor_ticket(cls, ticket_id):
        duration = 10  # Duration in seconds
        interval = 2  # Interval in seconds
        end_time = time.time() + duration
        flag = True

        while time.time() < end_time and flag:
            ticket_status = cls.get_ticket_by_id(ticket_id)
            status = ticket_status["status"]
            if ticket_status == "closed":
                flag = False
            logger.info(f"monitoring ticket number: {ticket_id} with status: {status}")
            await asyncio.sleep(interval)
from flask import jsonify, Flask, Blueprint

from data.ticket_manager import TicketManager

app = Flask(__name__)

api_th = Blueprint('api_th', __name__)


@api_th.route('/ticket_status/<string:ticket_id>')
def get_ticket_status(ticket_id):
    ticket = TicketManager.get_ticket_by_id(ticket_id)

    # If the ticket ID is found, return the ticket data
    if ticket is not None:
        return jsonify(ticket)

    # If the ticket ID is not found, return an error message
    return jsonify({"error": "Ticket not found."}), 404



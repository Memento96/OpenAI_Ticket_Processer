import json
from flask import Blueprint, request

from helper.helpers import get_bot_id, get_location_string, generate_ticket
from service.openai_utils import openai_complete
from data.ticket_manager import TicketManager

api_bp = Blueprint('api', __name__)

# This is used to pass the context included in the .txt
context_path = "context/chat_system_context_.txt"
with open(context_path, "r") as file:
    prompt_txt = file.read()

# Heartbeat API | I created a dummy Json
heartbeat_data_path = "data/heartbeat_data.json"
with open(heartbeat_data_path, 'r') as file:
    json_string = file.read()

heartbeat_dictionary = json.loads(json_string)


@api_bp.route('/submit_report', methods=['POST'])
def process_report():
    # This variable simulates the report sent from the view
    data = request.get_json()

    # Extract the required information from the report JSON
    report = data['report']
    bot_id = get_bot_id(heartbeat_dictionary) # bot's ID from the Kiwi's heartbeat JSON
    bot_location = get_location_string(heartbeat_dictionary) # bot's location from the Kiwi's heartbeat JSON
    ticket_id = generate_ticket() # Random number generated for the ticket

    # Generate the prompts for OpenAI GPT-3.5
    prompt_1 = f"Context: {prompt_txt}\n\n"
    prompt_2 = f"Bot ID: {bot_id}\n\n"
    prompt_3 = f"Bot Location: {bot_location}\n\n"
    prompt_4 = f"Ticket ID: {ticket_id}\n\n"
    prompt_5 = f"Report: {report}\n\n"

    # Concatenate all prompts into a single string
    chat_prompt = prompt_1 + prompt_2 + prompt_3 + prompt_4 + prompt_5

    # Converting the string message from OpenAI to a JSON
    chatGPT_response = openai_complete(chat_prompt)
    json_data = json.loads(chatGPT_response)
    formatted_json = json.dumps(json_data, indent=4)

    final_json = json.loads(formatted_json)


    # We could use a connection to a Database if needed, but for practical matters I will use local storage.
    TicketManager.append_ticket(final_json)


    return final_json

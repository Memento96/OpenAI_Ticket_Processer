import json
import random


# Helper function to generate a unique ticket ID
def generate_ticket():
    random_number = random.randint(0, 99999)
    return random_number

# Helper function to get the bot's location
def get_location_string(bot_api):
    try:
        bot_api_json = json.dumps(bot_api)  # Convert dictionary to JSON string
        data = json.loads(bot_api_json)
        lat = data["location"]["lat"]
        lon = data["location"]["lon"]
        location_string = f"Latitude: {lat}, Longitude: {lon}"
        return location_string
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
        return None

# Helper function to get the bot ID from another API
def get_bot_id(bot_api):
    # Make a request to the API endpoint that provides the Kiwibot's heartbeat
    try:
        bot_api_json = json.dumps(bot_api)
        data = json.loads(bot_api_json)
        bot_id = data['bot_id']
        return bot_id
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
        return None
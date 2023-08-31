# Import the required modules
import os
import sys
import json
import random
import logging
import requests

# Import the chat mode module
from chat_mode import ChatMode

# Set the logging level
logging.basicConfig(level=logging.INFO)

# Create a chat mode object
chat_mode = ChatMode()

# Load the chat settings from a JSON file
with open('chat_settings.json', 'r') as f:
    chat_settings = json.load(f)

# Get the chat mode name from the command line argument
chat_mode_name = sys.argv[1]

# Check if the chat mode name is valid
if chat_mode_name not in chat_settings['modes']:
    logging.error(f'Invalid chat mode name: {chat_mode_name}')
    sys.exit(1)

# Set the chat mode parameters
chat_mode.set_parameters(chat_settings['modes'][chat_mode_name])

# Start a new conversation with the user
chat_mode.start_conversation()

# Loop until the conversation ends
while not chat_mode.is_conversation_ended():
    # Get the user's message from the standard input
    user_message = input()
    # Process the user's message and generate a response
    chat_mode.process_message(user_message)
    # Print the response to the standard output
    print(chat_mode.get_response())

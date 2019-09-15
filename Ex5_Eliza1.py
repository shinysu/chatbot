'''Asking questions is a great way to create an engaging conversation. Here, you'll create the very first hint of
ELIZA's famous personality, by responding to statements with a question and responding to questions with answers.'''

#Example 4
# Import the random module
import random

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# A dictionary of responses with "question" and "statement" as keys and lists of appropriate responses as values
responses = {
  "statement": [
       'tell me more!',
       'why do you think that?',
       'how long have you felt this way?',
       'I find that extremely interesting',
       'can you back that up?',
       'oh wow!',
       ':)'
   ],
  "question": ["I don't know :(", 'you tell me!'
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")
import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = google_api_key)

# Define your system instruction
# This tells the model how to behave for all following prompts.
system_instruction = "You are a person named Bodhit who speaks hindi as well as english. You are from India and you are a software engineer. You analyze chat history and respond like Bodhit. Continue the conversation, single message only, and that too in short. Only respond in one language, according to the context and the earlier conversations in either hindi or english, not both."

# Initialize the model with the system instruction
model = genai.GenerativeModel(
    model_name = 'gemini-1.5-flash-latest',
    system_instruction = system_instruction
)

def check_last_sender(chat_history, my_name="Bodhit"):
    """
    Checks if the last message in the chat history was sent by you.
    Handles chat formats with timestamps like '[timestamp] Name: message'.

    Args:
        chat_history (str): The entire chat history as a single string.
        my_name (str): The name used to identify your own messages (the bot).

    Returns:
        bool: True if the last message is from 'my_name', False otherwise.
    """
    # Split the chat history into lines and remove any empty or whitespace-only lines
    lines = [line for line in chat_history.strip().split('\n') if line.strip()]
    
    # If the chat history is empty, we can assume it's not from you.
    if not lines:
        return False
        
    # Get the very last message from the list of lines
    last_message = lines[-1]
    
    # Check for the timestamp format "[...]" which is common in chat logs.
    if ']' in last_message:
        # Split the message after the timestamp to isolate the sender and message
        parts = last_message.split(']', 1)
        if len(parts) > 1:
            # The sender part is the second element. e.g., " Bodhit: Hello"
            sender_part = parts[1].strip()
            # Check if this part starts with your name followed by a colon
            if sender_part.startswith(f"{my_name}:"):
                print(f"Last message is from {my_name}. Waiting for a new message.")
                return True

    # If this logic doesn't find a match (e.g., different format),
    # we can fall back to the simple check just in case.
    if last_message.strip().startswith(my_name):
        print(f"Last message is from {my_name} (fallback check). Waiting.")
        return True

    print("Last message is from sender. Generating response...")
    return False

# Click on the icon at co-ordinates (1277, 1042)
pyautogui.click(1277, 1042)
time.sleep(1) # Wait for 1 second to ensure the click is registered

while True:
    try:
        # Drag the mouse from (680, 194) to (1910, 997) to select the text
        pyautogui.moveTo(680, 194)
        pyautogui.dragTo(1910, 997, duration=1.0, button="left")

        # Copy the selected text to the Clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1) # Wait for 1 second to ensure the copy command is completed

        # Retreive the text from the clipboard and store it in a variable
        chat_history = pyperclip.paste()

        # Click somewhere so that the selected text gets deselected.
        pyautogui.click(1875, 382)

        # Check who sent the last message
        # If the last message is from you (Bodhit), skip the rest of the loop and wait before checking again.
        if check_last_sender(chat_history, "Bodhit"):
            time.sleep(5) # Wait for 5 seconds before the next check
            continue

        # The rest of the code only runs if the last message is NOT from you

        # print(chat_history) # Uncomment for debugging if needed

        response = model.generate_content(chat_history)
        print("Bot Response: ", response.text)

        # Copy the response to paste it in the chatbox
        pyperclip.copy(response.text)

        # Click at the coordinates (1309, 972)
        pyautogui.click(1309,972)
        time.sleep(1) # Wait for 1 second to ensure the click is registered.

        # Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1) # Wait for 1 second to ensure the paste command is completed.

        # Press Enter
        pyautogui.press('enter')
        time.sleep(2) # Add a small delay after sending to avoid instantly re-reading its own message

    except Exception as e:
        print(f"An error occurred: {e}")
        # Wait for a moment before retrying to avoid spamming errors
        time.sleep(10)
